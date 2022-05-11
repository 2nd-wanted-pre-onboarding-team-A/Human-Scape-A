# Generated by Django 3.2.6 on 2022-05-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='department',
            field=models.CharField(max_length=100, null=True, verbose_name='진료과'),
        ),
        migrations.AlterField(
            model_name='research',
            name='duration',
            field=models.CharField(blank=True, max_length=100, verbose_name='연구 기간'),
        ),
        migrations.AlterField(
            model_name='research',
            name='institute',
            field=models.CharField(max_length=100, null=True, verbose_name='연구 책임 기관'),
        ),
        migrations.AlterField(
            model_name='research',
            name='number',
            field=models.CharField(max_length=100, unique=True, verbose_name='과제 번호'),
        ),
        migrations.AlterField(
            model_name='research',
            name='scope',
            field=models.CharField(max_length=100, null=True, verbose_name='연구 범위'),
        ),
        migrations.AlterField(
            model_name='research',
            name='stage',
            field=models.CharField(max_length=100, null=True, verbose_name='임상 시험 단계'),
        ),
        migrations.AlterField(
            model_name='research',
            name='target',
            field=models.CharField(blank=True, max_length=100, verbose_name='전체 목표 연구 대상자 수'),
        ),
        migrations.AlterField(
            model_name='research',
            name='title',
            field=models.CharField(max_length=300, verbose_name='과제명'),
        ),
        migrations.AlterField(
            model_name='research',
            name='type',
            field=models.CharField(max_length=100, null=True, verbose_name='연구 종류'),
        ),
    ]