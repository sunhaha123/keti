# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-18 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yundongyuan', '0006_auto_20180604_2100'),
        ('events', '0002_auto_20180618_1733'),
        ('xunlian', '0006_auto_20180604_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='XunlianSum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riqi', models.DateField(blank=True, default='2010-01', null=True, verbose_name='训练日期')),
                ('sum', models.IntegerField(verbose_name='训练总次数')),
                ('xiangmu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Xiangmu', verbose_name='体操项目')),
                ('xingming', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yundongyuan.Athlete', verbose_name='队员姓名')),
            ],
            options={
                'verbose_name': '训练总数统计',
                'verbose_name_plural': '训练总数统计',
            },
        ),
        migrations.RemoveField(
            model_name='xunliancj',
            name='xiangmu',
        ),
        migrations.RemoveField(
            model_name='xunliancj',
            name='xingming',
        ),
        migrations.RemoveField(
            model_name='xunliansh',
            name='xingming',
        ),
        migrations.DeleteModel(
            name='XunlianCj',
        ),
        migrations.DeleteModel(
            name='XunlianSh',
        ),
    ]