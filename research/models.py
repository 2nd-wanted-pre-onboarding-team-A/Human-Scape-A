from django.db import models
from core.models import TimeStampModel

class Research(TimeStampModel):
    # 과제 번호
    number = models.CharField(max_length=100, unique=True)
    # 과제명
    title = models.CharField(max_length=300)
    # 진료과
    department = models.CharField(max_length=100, null=True)
    # 연구 책임 기관
    institute = models.CharField(max_length=100, null=True)
    # 전체 목표 연구 대상자 수
    target = models.CharField(max_length=100, blank=True)
    # 연구 기간
    duration = models.CharField(max_length=100, blank=True)
    # 연구 종류
    type = models.CharField(max_length=100, null=True)
    # 임상 시험 단계
    stage = models.CharField(max_length=100, null=True)
    # 연구 범위
    scope = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'research'


