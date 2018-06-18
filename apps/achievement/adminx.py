# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import ChengjiDate
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime

class  ChengjiDateAdmin(object):
    list_display = ['athlete','date','xiangmu','mingcheng','xiangmu','jibie','nandufen','wanchengfen','zongfen']
    # search_fields = ['xingming_id','riqi','xiangmu','content']
    list_filter = ['athlete','date','xiangmu','mingcheng','xiangmu','jibie','nandufen','wanchengfen','zongfen']
    model_icon = 'fa fa-trophy'
    import_excel=True
    data_charts = {
            "user_count": {'title': u"训练-难度分", "x-field": "date", "y-field": ("nandufen", ), "order": ('date',)},
            "user_count2": {'title': u"训练-完成分", "x-field": "date", "y-field": ("wanchengfen",), "order": ('date',)},
            "user_count3": {'title': u"训练-总分", "x-field": "date", "y-field": ("zongfen",), "order": ('date',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
        }
    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            table = wb.sheets()[0]
            row = table.nrows
            sql_list = []
            sport_id_list = []
            for i in range(1, row):
                col = table.row_values(i)
                for j in range(4,7):
                     if col[j]=='':
                             col[j]=0
                sql = ChengjiDate(
                    athlete_id=col[0],
                    date=str(datetime(*xldate_as_tuple(col[1], 0)))[0:10],
                    mingcheng=col[2],
                    xiangmu_id=col[3],
                    nandufen=col[4],
                    wanchengfen=col[5],
                    zongfen=col[6]
                )
                sql_list.append(sql)
            ChengjiDate.objects.bulk_create(sql_list)
        return super(ChengjiDateAdmin, self).post(request, args, kwargs)






# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(ChengjiDate,ChengjiDateAdmin)
# xadmin.site.register(ChengjiSh,ChengjiShAdmin)