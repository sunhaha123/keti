# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Xiangmu(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    # birthday = models.DateField(null=True, blank=True, verbose_name=u'生日', default='2010-01-01')
    # gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default=u"male",
    #                           verbose_name=u'性别')
    # address = models.CharField(max_length=100, default=u'', verbose_name=u'地址')
    # mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')



    class Meta:
        verbose_name = u'运动项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name