# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from yundongyuan.models import Athlete
from events.models import Xiangmu

# Create your models here.
class XunlianDate(models.Model):
    xingming = models.ForeignKey(Athlete, verbose_name=u'队员姓名')
    riqi = models.DateField(null=True, blank=True, verbose_name=u'训练日期', default='2010-01-01')
    xiangmu = models.ForeignKey(Xiangmu, verbose_name=u'体操项目')
    content = models.CharField(max_length=50, default=u'', verbose_name=u'训练内容')

    class Meta:
        verbose_name = u'训练记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.xingming.name


class XunlianSh(models.Model):
    xingming = models.ForeignKey(Athlete, verbose_name=u'队员姓名')
    riqi = models.DateField(null=True, blank=True, verbose_name=u'训练日期', default='2010-01-01')
    gaotong = models.FloatField(verbose_name=u'睾酮')

    class Meta:
        verbose_name = u'训练-生化'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.xingming.name

class XunlianCj(models.Model):
    xingming = models.ForeignKey(Athlete, verbose_name=u'队员姓名')
    riqi = models.DateField(null=True, blank=True, verbose_name=u'训练日期', default='2010-01-01')
    mingcheng = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'赛事名称')
    xiangmu = models.ForeignKey(Xiangmu, verbose_name=u'体操项目')
    tianshu = models.IntegerField(verbose_name=u'累计训练天数')
    nandufen = models.FloatField(verbose_name=u'难度分')
    wanchengfen = models.FloatField(verbose_name=u'完成')
    zongfen = models.FloatField(verbose_name=u'总分')
    sbcishu = models.IntegerField(verbose_name=u'失败次数')
    sbyuanyin = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'失败原因')

    class Meta:
        verbose_name = u'训练-成绩'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.xingming.name