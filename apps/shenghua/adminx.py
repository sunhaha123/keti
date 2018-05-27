# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import ShenghuaDate
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime

class  ShenghuaDateAdmin(object):
    list_display = ['athlete','date','gaotong','pizhichun','niaosudan','jisuanjimei','tc','yichang']
    # search_fields = ['xingming_id','riqi','xiangmu','content']
    list_filter = ['athlete','date','gaotong','pizhichun','niaosudan','jisuanjimei','tc','yichang']
    model_icon = 'fa fa-tint'
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
                sql = ShenghuaDate(
                    athlete_id=col[0],
                    date=str(datetime(*xldate_as_tuple(col[1], 0)))[0:10],
                    gaotong=col[2],
                    pizhichun=col[3],
                    niaosudan=col[4],
                    jisuanjimei=col[5],
                    tc=col[6],
                )
                sql_list.append(sql)
            ShenghuaDate.objects.bulk_create(sql_list)
        return super(ShenghuaDateAdmin, self).post(request, args, kwargs)
# class  XunlianShAdmin(object):ma
#     list_display = ['xingming','riqi','gaotong']
#     # search_fields = ['xingming','riqi','gaotong']
#     list_filter = ['xingming','riqi','gaotong']
#     data_charts = {
#             "user_count": {'title': u"训练-生化", "x-field": "riqi", "y-field": ("gaotong", ), "order": ('riqi',)},
#             # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
#         }

# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(ShenghuaDate,ShenghuaDateAdmin)
# xadmin.site.register(XunlianSh,XunlianShAdmin)