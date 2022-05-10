import requests, datetime

from research.models import Research
from my_settings import OPEN_API_SECRET_KEY

OPEN_API_URL = 'https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887'
OPEN_API_SECRET_KEY = OPEN_API_SECRET_KEY

def get_count():
    params = {
        'serviceKey' : OPEN_API_SECRET_KEY
    }
    response = requests.get(OPEN_API_URL, params=params).json()

    return response['totalCount']

def batch_task():
    params = {
        'page' : 1,
        'perPage' : get_count(),
        'serviceKey' : OPEN_API_SECRET_KEY
    }

    response = requests.get(OPEN_API_URL, params=params).json()

    for study in response['data']:
        number = study['과제번호']

        Research.objects.get_or_create(
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
    print('DB insert OK')
   
