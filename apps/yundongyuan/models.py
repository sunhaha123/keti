# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from users.models import UserProfile

# Create your models here.
class Athlete(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name=u'出生年月', default='2010-01-01')
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default=u"male",
                              verbose_name=u'性别')
    coach = models.ForeignKey(UserProfile, verbose_name=u'主管教练', default='1')
    address = models.CharField(max_length=100,null=True, blank=True, verbose_name=u'地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')
    join_date = models.DateField(null=True, blank=True, verbose_name=u'入队年月', default='2012-01-01')
    character = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'特点')
    achievement = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'历年成绩')
    is_actice = models.BooleanField(default=True,verbose_name=u'在役')


    class Meta:
        verbose_name = u'运动员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name