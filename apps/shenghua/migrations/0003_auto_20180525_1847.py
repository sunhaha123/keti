# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-25 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shenghua', '0002_auto_20180525_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shenghuadate',
            name='yichang',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='异常数据说明'),
        ),
    ]
