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
    list_display = ['xingming','riqi','gaotong']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','gaotong']
    # data_charts = {
    #         "user_count": {'title': u"训练-生化", "x-field": "riqi", "y-field": ("gaotong", ), "order": ('riqi',)},
    #         # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    #     }

class  XunlianCjAdmin(object):
    list_display = ['xingming','riqi','mingcheng','xiangmu','tianshu','nandufen','wanchengfen','zongfen','sbcishu','sbyuanyin']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','mingcheng','xiangmu','tianshu','nandufen','wanchengfen','zongfen','sbcishu','sbyuanyin']
    # data_charts = {
    #         "user_count": {'title': u"训练-成绩", "x-field": "tianshu", "y-field": ("nandufen","wanchengfen" ), "order": ('riqi',)},
    #         # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    #     }

class  ChengjiShAdmin(object):
    list_display = ['xingming','riqi','gaotong','nandufen','wanchengfen','zongfen']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','gaotong','nandufen','wanchengfen','zongfen']

    # data_charts = {
    #         "user_count": {'title': u"训练-生化", "x-field": "riqi", "y-field": ("gaotong", ), "order": ('riqi',)},
    #         # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    #     }


xadmin.site.register(XunlianSh,XunlianShAdmin)
xadmin.site.register(XunlianCj,XunlianCjAdmin)
xadmin.site.register(ChengjiSh,ChengjiShAdmin)