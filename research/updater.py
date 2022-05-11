from time import sleep
import logging
import logging.handlers

import requests
import os

from research.models import Research
try:
    from my_settings import OPEN_API_SECRET_KEY
except:
    OPEN_API_SECRET_KEY = os.environ['OPEN_API_SECRET_KEY']

OPEN_API_URL = 'https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887'
OPEN_API_SECRET_KEY = OPEN_API_SECRET_KEY

def batch_task_logger(success_count, failure_count):
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] >> %(message)s')
    streamHandler = logging.StreamHandler()
    fileHandler = logging.FileHandler('./batch_task.log')
    streamHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)
    logger.setLevel(level=logging.DEBUG)
    logger.info(f'{success_count} rows created, {failure_count} rows failed.')

def get_count():
    """
        전체 데이터의 개수를 리턴
    """
    params = {
        'serviceKey' : OPEN_API_SECRET_KEY
    }
    response = requests.get(OPEN_API_URL, params=params).json()

    return response['totalCount']

def batch_task():
    """
        get_count()에서 가져온 전체 데이터의 개수만큼 DB에 적재하는 batch task
    """
    # test를 위한 for문
    for i in range (1, int(get_count()/5)+1):
        params = {
            # 'page' : 1,
            # 'perPage' : get_count(),
            # 'serviceKey' : OPEN_API_SECRET_KEY
            'page' : i,
            'perPage' : 5,
            'serviceKey' : OPEN_API_SECRET_KEY
        }

        print(i)
        success_count = 0
        failure_count = 0
        response = requests.get(OPEN_API_URL, params=params).json()

        for study in response['data']:
            number = study['과제번호']
            
            if not Research.objects.filter(number=number).exists():
                # 과제 번호가 등록되어 있지 않은 경우
                Research.objects.create(
                    number      = number,
                    title       = study['과제명'],
                    department  = study['진료과'] if study['진료과'] else '',
                    institute   = study['연구책임기관'] if study['연구책임기관'] else '',
                    target      = study['전체목표연구대상자수'] if study['전체목표연구대상자수'] else '',
                    duration    = study['연구기간'] if study['연구기간'] else '',
                    type        = study['연구종류'] if study['연구종류'] else '',
                    stage       = study['임상시험단계(연구모형)'] if study['임상시험단계(연구모형)'] else '',
                    scope       = study['연구범위'] if study['연구범위'] else '',
                )
                success_count += 1
            else:
                # 이미 과제 번호가 등록되어 있는 경우
                failure_count += 1

        # API 1회 요청에 대한 성공, 실패 row개수를 로깅
        batch_task_logger(success_count, failure_count)
        sleep(5) # Interval과 동일한 동작을 하기위해 추가
   
