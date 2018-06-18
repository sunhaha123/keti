# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import XunlianDate,XunlianSum
from datetime import datetime
from xlrd import xldate_as_tuple
import xlrd

class  XunlianDateAdmin(object):
    list_display = ['xingming','riqi','xiangmu','content']
    # search_fields = ['xingming_name',]
    list_filter = ['xingming','riqi','xiangmu','content']
    model_icon = 'fa fa-align-left'
    import_excel=True
    def post(self, request, *args, **kwargs):
            if 'excel' in request.FILES:
                wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
                table = wb.sheets()[0]
                row = table.nrows
                sql_list = []
                sport_id_list = []
                for i in range(1, row):
                    col = table.row_values(i)
                    # col[1] = str(datetime(*xldate_as_tuple(col[1], 0))),
                    sql = XunlianDate(
                        xingming_id=col[0],
                        riqi=str(datetime(*xldate_as_tuple(col[1], 0)))[0:10],
                        xiangmu_id=col[2],
                        content=col[4]
                    )
                    sql_list.append(sql)
                XunlianDate.objects.bulk_create(sql_list)
            return super(XunlianDateAdmin, self).post(request, args, kwargs)

class XunlianSumAdmin(object):
    list_display = ['xingming', 'riqi', 'xiangmu', 'sum']
    # search_fields = ['xingming_name',]
    list_filter = ['xingming', 'riqi', 'xiangmu', 'sum']


    data_charts = {
        "user_count": {'title': u"训练次数统计(每月)", "x-field": "riqi", "y-field": ("sum",), "order": ('riqi',)},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}


    }

# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(XunlianDate,XunlianDateAdmin)
xadmin.site.register(XunlianSum,XunlianSumAdmin)
# xadmin.site.register(XunlianCj,XunlianCjAdmin)