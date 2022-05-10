from django.db import models
from core.models import TimeStampModel

class Research(TimeStampModel):
    number      = models.CharField(max_length=100, unique=True, verbose_name='과제 번호')
    title       = models.CharField(max_length=300, verbose_name='과제명')
    department  = models.CharField(max_length=100, null=True, verbose_name='진료과')
    institute   = models.CharField(max_length=100, null=True, verbose_name='연구 책임 기관')
    target      = models.CharField(max_length=100, blank=True, verbose_name='전체 목표 연구 대상자 수')
    duration    = models.CharField(max_length=100, blank=True, verbose_name='연구 기간')
    type        = models.CharField(max_length=100, null=True, verbose_name='연구 종류')
    stage       = models.CharField(max_length=100, null=True, verbose_name='임상 시험 단계')
    scope       = models.CharField(max_length=100, null=True, verbose_name='연구 범위')

    class Meta:
        db_table = 'research'


