# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-17 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tubiao1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='标题')),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='图表')),
                ('introduce', models.CharField(blank=True, max_length=50, null=True, verbose_name='图表简介')),
            ],
            options={
                'verbose_name': '成绩对比图',
                'verbose_name_plural': '成绩对比图',
            },
        ),
    ]
