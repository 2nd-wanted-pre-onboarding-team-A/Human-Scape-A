import requests
import os

from .models import Paper, TotalNumber
try:
    from my_settings import OPEN_API_SECRET_KEY_CHALLENGE
except:
    OPEN_API_SECRET_KEY_CHALLENGE = os.environ['OPEN_API_SECRET_KEY_CHALLENGE']

OPEN_API_URL = 'http://apis.data.go.kr/1471000/MdcinClincTestInfoService01/getMdcinClincTestInfoList01'
OPEN_API_SECRET_KEY_CHALLENGE = OPEN_API_SECRET_KEY_CHALLENGE


class BatchTask:
    '''
    writer: 윤상민
    도전과제 문제이해를 잘못하여 만들었던 코드입니다. 그래서 Scheduler부분의 Time간격을 길게 해두어
    사실상 작동하지 않게 만들었습니다.
    '''
    def get_count(self):
        params = {
            'serviceKey' : OPEN_API_SECRET_KEY_CHALLENGE,
            'approval_time' : '', 
            'goods_name' : '', 
            'pageNo' : '1', 
            'numOfRows' : '1', 
            'type' : 'json'
            }
        response = requests.get(OPEN_API_URL, params=params)
        count = int(response.json()['body']['totalCount'])
        return count

    def get_data(self, page=1, rows=100):
        '''
            공공데이터 API로부터 data를 가져옴
        '''
        params = {
            'serviceKey' : OPEN_API_SECRET_KEY_CHALLENGE,
            'approval_time' : '', 
            'goods_name' : '', 
            'pageNo' : f'{page}', 
            'numOfRows' : f'{rows}', 
            'type' : 'json'
            }
        response = requests.get(OPEN_API_URL, params=params).json()
        return response

    def compare_data(self):
        '''
        변수로 받은 자료와 데이터베이스 자료 비교
        방법1. Total count갯수 비교
        방법2. 마지막 업데이트 자료 비교
        '''
        pass

    def is_not_updated(self):
        '''
        업데이트확인
        '''
        pass
    
    def update_data(self, data):
        '''
        DB적재
        '''
        items = data['body']['items']
        for item in items:
            Paper.objects.get_or_create(
                APPLY_ENTP_NAME = item['APPLY_ENTP_NAME'],
                APPROVAL_TIME = item['APPROVAL_TIME'],
                LAB_NAME = item['LAB_NAME'],
                GOODS_NAME = item['GOODS_NAME'],
                CLINIC_EXAM_TITLE = item['CLINIC_EXAM_TITLE'],
                CLINIC_STEP_NAME = item['CLINIC_STEP_NAME'],
            )

    def batch_task(self):
        
        #갯수세고
        total_count = self.get_count()

        #데이터겟하고
        data = self.get_data()

        #이전에 조사했던 마지막 기록이 없다면 DB에 저장해두고
        if TotalNumber.objects.all().count() == 0:
            TotalNumber.objects.create(totalCount=total_count)

        #데이터의 총 갯수 * 0.5 > DB에 저장된 총 갯수라면 전수조사를 돌리고 종료
        start_count = Paper.objects.all().count()
        if total_count * 0.5 > start_count:
            print("DB자료가 API자료의 개수의 50%미만이므로 전수조사를 진행합니다.")
            print(f"총{total_count}개의 자료를 DB와 비교할 예정이며 현재 DB에 저장된 자료의 수는 {start_count}입니다.")
            # try:
            for i in range((total_count //100) + 1 ):
                data = self.get_data(i+1, 100)
                self.update_data(data)
                print(f"{i}/{(total_count //100) + 1}진행중")
            # except:
            #     print("입력충돌")
            end_count = Paper.objects.all().count()
            print(f"전수조사가 종료되었으며 경과시간은 00이고 중복을 제외하고 DB에 총 입력된 자료의 개수는 {end_count - start_count}입니다.")
            return print("-------오늘의 스케쥴작업 종료--------- ")
            
        
        #비교1) 마지막으로 받았던 api의 자료 갯수와 이번에 받은 자료 갯수를 확인하고
        if TotalNumber.objects.last().totalCount != total_count:
            #다르다면
            '''
            부족한 부분만 연산하는 코드를 집어넣어야 하지 않겠음? 이 부분 고민중
            ''' 
            pass
        
        #비교2) 마지막 데이터와 저장된 데이터 비교 및 마지막 데이터의 총 갯수 확인
        # have_to_update = False
        # data_last = self.get_data(total_count, 1)
        # try:
        #     last_id = Paper.objects.all().last().id
        #     self.update_data(data_last)
        #     if Paper.objects.last().id > last_id:
        #         have_to_update = True
        # except:
        #     have_to_update = True
        '''
        이 부분도 다시 구현해야함
        '''
        
        # 두 번의 비교 검증으로 업데이트요소가 발견되었다면 부족한 갯수만큼 조사
        '''
        이 부분 다시 구현해야함. 
        '''
        # if have_to_update:
        #     try:
        #         for i in range((total_count //100) + 1 ):
        #             data = self.get_data(i+1, 100)
        #             self.update_data(data)
        #             print("포문다돌았다")
        #     except:
        #         print("에러떴다")
        # else:
        #     print("업데이트할 항목이 없습니다.")
        
        print("오늘의 스케쥴 종료")

