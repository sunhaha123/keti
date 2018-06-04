# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import XunlianDate, XunlianSh,XunlianCj
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple


class  XunlianDateAdmin(object):
    list_display = ['xingming','riqi','xiangmu','content']
    # search_fields = ['xingming_id','riqi','xiangmu','content']
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

class  XunlianShAdmin(object):
    list_display = ['xingming','riqi','gaotong']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','gaotong']
    data_charts = {
            "user_count": {'title': u"训练-生化", "x-field": "riqi", "y-field": ("gaotong", ), "order": ('riqi',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
        }

class  XunlianCjAdmin(object):
    list_display = ['xingming','riqi','mingcheng','xiangmu','tianshu','nandufen','wanchengfen','zongfen','sbcishu','sbyuanyin']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','mingcheng','xiangmu','tianshu','nandufen','wanchengfen','zongfen','sbcishu','sbyuanyin']
    data_charts = {
            "user_count": {'title': u"训练-成绩", "x-field": "tianshu", "y-field": ("nandufen","wanchengfen" ), "order": ('riqi',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
        }

# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(XunlianDate,XunlianDateAdmin)
# xadmin.site.register(XunlianSh,XunlianShAdmin)
# xadmin.site.register(XunlianCj,XunlianCjAdmin)