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
                for j in range(2,7):
                     if col[j]=='':
                             col[j]=0
                sql = ShenghuaDate(
                    athlete_id=col[0],
                    date=str(datetime(*xldate_as_tuple(col[1], 0)))[0:10],
                    gaotong=float(col[2]),
                    pizhichun=float(col[3]),
                    niaosudan=float(col[4]),
                    jisuanjimei=float(col[5]),

                    tc=col[6],
                    yichang=col[9]
                )
                sql_list.append(sql)
            ShenghuaDate.objects.bulk_create(sql_list)
        return super(ShenghuaDateAdmin, self).post(request, args, kwargs)

    data_charts = {
            "user_count": {'title': u"生化指标-睾酮", "x-field": "date", "y-field": ("gaotong", ), "order": ('date',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
            "user_count2": {'title': u"生化指标-皮质醇", "x-field": "date", "y-field": ('pizhichun'), "order": ('date',)},
            "user_count3": {'title': u"生化指标-尿素氮", "x-field": "date", "y-field": ( 'niaosudan', ), "order": ('date',)},
            "user_count4": {'title': u"生化指标-肌酸激酶", "x-field": "date", "y-field": ( 'jisuanjimei', ), "order": ('date',)},
            "user_count5": {'title': u"生化指标-TC", "x-field": "date", "y-field": ( 'tc'), "order": ('date',)},

    }

# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(ShenghuaDate,ShenghuaDateAdmin)
# xadmin.site.register(XunlianSh,XunlianShAdmin)