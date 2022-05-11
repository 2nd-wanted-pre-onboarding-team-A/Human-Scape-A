from django.db import models
from core.models import TimeStampModel


class Paper(TimeStampModel):
    APPLY_ENTP_NAME = models.CharField(max_length=500, default='', null=True, verbose_name='신청자')
    APPROVAL_TIME = models.DateTimeField(max_length=100, default='', null=True, verbose_name='승인일')
    LAB_NAME = models.CharField(max_length=2000, default='', null=True, verbose_name='실시기관명')
    GOODS_NAME = models.CharField(max_length=1000, default='', null=True, verbose_name='제품명')
    CLINIC_EXAM_TITLE = models.CharField(max_length=2000, default='', null=True, verbose_name='시험제목')
    CLINIC_STEP_NAME = models.CharField(max_length=500, default='', null=True, verbose_name='단계')

    class Meta:
        db_table = 'paper'
        ordering = ['-updated_at']


class TotalNumber(TimeStampModel):
    totalCount = models.IntegerField(verbose_name='마지막으로 기록된 전체 결과 수')
    
    class Meta:
        db_table = 'total_number'