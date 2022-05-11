import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q
from datetime         import datetime, timedelta, timezone

from research.models import Research

class PublicDataListView(View):
    def get(self, request):
        try:
            sorting = request.GET.get('sort', 'latest')
            search = request.GET.get('search')
            update_week = request.GET.get('week')
            OFFSET = int(request.GET.get('offset',0))
            LIMIT = int(request.GET.get('limit', 10))

            q = Q()
            if search:
                q &= Q(title__icontains = search)
            
            if update_week:
                q &= Q(updated_at__gte = (timezone.now() - timedelta(days=7)))

            sort = {
                'latest' : 'created_at',
                'oldest' : '-created_at',
                'update' : 'updated_at'
            }

            research_data_set = Research.objects.filter(q)\
                                                .order_by(sort[sorting])[OFFSET:OFFSET+LIMIT]

            result = {
                'data' : [{
                    '과제명' : research_data.title,
                    '과제 번호' : research_data.number,
                    '연구 기간' : research_data.duration,
                    '연구 범위' : research_data.scope,
                    '연구 종류' : research_data.type,
                    '연구 책임 기관' : research_data.institute,
                    '임상 시험 단계': research_data.stage,
                    '전체 목표 연구 대상자 수' : research_data.target,
                    '진료과' : research_data.department,
                }for research_data in research_data_set]
            }
            return JsonResponse({'result' : result}, status=200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class PublicDataDetailView(View):
    def get(self, request, id):
        try:
            if not Research.objects.filter(id=id).exists():
                return JsonResponse({'message':'DOES_NOT_EXIST'}, status=404)

            data = Research.objects.get(id=id)

            result = {
                    '과제명' : data.title,
                    '과제 번호' : data.number,
                    '연구 기간' : data.duration,
                    '연구 범위' : data.scope,
                    '연구 종류' : data.type,
                    '연구 책임 기관' : data.institute,
                    '임상 시험 단계': data.stage,
                    '전체 목표 연구 대상자 수' : data.target,
                    '진료과' : data.department,
            }

            return JsonResponse({'result':result}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)    
