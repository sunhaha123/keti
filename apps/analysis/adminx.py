# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import  XunlianSh,XunlianCj,ChengjiSh
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple



class  XunlianShAdmin(object):
    list_display = ['xingming','riqi','gaotong','pizhichun','niaosudan','jisuanjimei']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','gaotong','pizhichun','niaosudan','jisuanjimei',]
    data_charts = {
            "user_count": {'title': u"训练（日期）-生化(睾酮)", "x-field": "riqi", "y-field": ("gaotong", ), "order": ('riqi',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
            "user_count2": {'title': u"训练（日期）-生化（皮质醇）", "x-field": "riqi", "y-field": ("pizhichun",), "order": ('riqi',)},
            "user_count3": {'title': u"训练（日期）-生化（尿素氮）", "x-field": "riqi", "y-field": ("niaosudan",), "order": ('riqi',)},
            "user_count4": {'title': u"训练（日期）-生化（肌酸激酶）", "x-field": "riqi", "y-field": ("jisuanjimei",), "order": ('riqi',)},
        # "user_count": {'title': u"训练（日期）-生化", "x-field": "riqi", "y-field": ("yichang",), "order": ('riqi',)},
        }

class  XunlianCjAdmin(object):
    list_display = ['xingming','riqi','mingcheng','xiangmu','tianshu','nandufen','wanchengfen','zongfen','sbcishu','sbyuanyin']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','mingcheng','xiangmu','tianshu','nandufen','wanchengfen','zongfen','sbcishu','sbyuanyin']
    data_charts = {
            "user_count": {'title': u"训练（天数）-成绩", "x-field": "tianshu", "y-field": ("nandufen","wanchengfen","zongfen" ), "order": ('riqi',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
        }

class  ChengjiShAdmin(object):
    list_display = ['xingming','riqi','gaotong','nandufen','wanchengfen','zongfen']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','gaotong','nandufen','wanchengfen','zongfen']

    data_charts = {
            "user_count": {'title': u"生化(睾酮)-成绩", "x-field": "gaotong", "y-field": ("nandufen","zongfen" ), "order": ('gaotong',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
        }


class  XunlianDateAdmin2(object):
    list_display = ['xingming','riqi','xiangmu','content']
    # search_fields = ['xingming_name',]
    list_filter = ['xingming','riqi','xiangmu','content']
    model_icon = 'fa fa-align-left'

xadmin.site.register(XunlianSh,XunlianShAdmin)
xadmin.site.register(XunlianCj,XunlianCjAdmin)
xadmin.site.register(ChengjiSh,ChengjiShAdmin)
# xadmin.site.register(XunlianDate,XunlianDateAdmin2)