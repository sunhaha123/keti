# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-04 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('yundongyuan', '0005_auto_20180527_1602'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChengjiDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default='2010-01-01', null=True, verbose_name='比赛日期')),
                ('mingcheng', models.CharField(blank=True, max_length=50, null=True, verbose_name='赛事名称')),
                ('jibie', models.CharField(choices=[('guoji', '国际'), ('quanguo', '全国'), ('shengji', '省级')], default='全国', max_length=50, verbose_name='赛事级别')),
                ('nandufen', models.FloatField(verbose_name='难度分')),
                ('wanchengfen', models.FloatField(verbose_name='完成')),
                ('zongfen', models.FloatField(verbose_name='总分')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yundongyuan.Athlete', verbose_name='运动员姓名')),
                ('xiangmu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Xiangmu', verbose_name='体操项目')),
            ],
            options={
                'verbose_name_plural': '运动成绩',
                'verbose_name': '运动成绩',
            },
        ),
    ]
