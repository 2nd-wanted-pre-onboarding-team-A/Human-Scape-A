import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q
from datetime         import datetime, timedelta

from research.models import Research


class PublicDataListView(View):
    """
    정렬기능, 제목 검색기능을 포함한 데이터 목록 조회 API
    Writer : 권은경
    Reviewer : 윤상민, 양수영
    """
    def get(self, request):
        try:
            sorting = request.GET.get('sort', 'id')
            search = request.GET.get('search')
            institute = request.GET.get('institute')
            OFFSET = int(request.GET.get('offset',0))
            LIMIT = int(request.GET.get('limit', 10))

            q = Q()

            if search:
                q &= Q(title__icontains = search)

            if institute:
                q &= Q(institute__icontains = institute)

            sort = {
                'latest' : '-updated_at',
                'oldest' : 'created_at',
                'id' : 'id'
            }

            search_data_set = Research.objects.filter(q)\
                                              .order_by(sort[sorting])[OFFSET:OFFSET+LIMIT]

            result = {
                'data' : [{
                    'id' : research_data.id,
                    '과제명' : research_data.title,
                    '과제 번호' : research_data.number,
                    '연구 기간' : research_data.duration,
                    '연구 범위' : research_data.scope,
                    '연구 종류' : research_data.type,
                    '연구 책임 기관' : research_data.institute,
                    '임상 시험 단계': research_data.stage,
                    '전체 목표 연구 대상자 수' : research_data.target,
                    '진료과' : research_data.department,
                }for research_data in search_data_set]
            }
            return JsonResponse({'result' : result}, status=200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)


class UpdateDataListView(View):
    """
    최근 일주일 동안 업데이트 된 데이터 목록 조회 API
    Writer : 권은경
    Reviewer : 윤상민, 양수영
    """
    def get(self, request):
        try:
            OFFSET = int(request.GET.get('offset',0))
            LIMIT = int(request.GET.get('limit', 10))
            now = datetime.now() 
            # now = datetime(year=2022, month=5, day=20) # 업데이트 결과 확인용 

            if not Research.objects.filter(updated_at__range=[now - timedelta(days=7), now]).exists():
                return JsonResponse ({'message' : '업데이트 된 정보가 없습니다.'}, status=404)

            weekly_updated = Research.objects.filter(
                             updated_at__range=[now - timedelta(days=7), now])\
                             .order_by('-updated_at')[OFFSET:OFFSET+LIMIT]

            result = {
                'data' : [{
                    'id' : research_data.id,
                    '과제명' : research_data.title,
                    '과제 번호' : research_data.number,
                    '연구 기간' : research_data.duration,
                    '연구 범위' : research_data.scope,
                    '연구 종류' : research_data.type,
                    '연구 책임 기관' : research_data.institute,
                    '임상 시험 단계': research_data.stage,
                    '전체 목표 연구 대상자 수' : research_data.target,
                    '진료과' : research_data.department,
                    '업데이트 시간' : research_data.updated_at,
                }for research_data in weekly_updated]
            }
            return JsonResponse({'result' : result}, status=200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)


class PublicDataDetailView(View):
    """
    연구 데이터 상세 정보 조회 API (id 기준)
    Writer : 권은경
    Reviewer : 윤상민, 양수영
    """
    def get(self, request, id):
        try:
            if not Research.objects.filter(id=id).exists():
                return JsonResponse({'message':'DOES_NOT_EXIST'}, status=404)

            data = Research.objects.get(id=id)

            result = {
                    'id' : data.id,
                    '과제명' : data.title,
                    '과제 번호' : data.number,
                    '연구 기간' : data.duration,
                    '연구 범위' : data.scope,
                    '연구 종류' : data.type,
                    '연구 책임 기관' : data.institute,
                    '임상 시험 단계': data.stage,
                    '전체 목표 연구 대상자 수' : data.target,
                    '진료과' : data.department,
                    '업데이트 시간' : data.updated_at,
            }

            return JsonResponse({'result':result}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

    """
    개발용 데이터 PATCH 함수 (업데이트 확인)
    Writer : 양수영
    Reviewer : 권은경, 윤상민
    """
    def patch(self, request, id):
            try:
                data = json.loads(request.body)
                research = Research.objects.get(id=id)

                title = data['title']
                # number = data['number'] # 수정 불가
                duration = data['duration']
                scope = data['scope']
                type = data['type']
                institute = data['institute']
                stage = data['stage']
                target = data['target']
                department = data['department']

                research.title = title
                research.duration = duration
                research.scope = scope
                research.type = type
                research.institute = institute
                research.stage = stage
                research.target = target
                research.department = department
                research.save()

                return JsonResponse({'message':'SUCCESS'}, status = 200)

            except KeyError:
                return JsonResponse({'message':'KEY_ERROR'}, status=400)

            except Research.DoesNotExist:
                return JsonResponse({'message':'RESEARCH_DOES_NOT_EXIST'}, status=404)
