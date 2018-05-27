# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import ChengjiDate, ChengjiSh
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime

class  ChengjiDateAdmin(object):
    list_display = ['athlete','date','xiangmu','mingcheng','xiangmu','jibie','nandufen','wanchengfen','zongfen']
    # search_fields = ['xingming_id','riqi','xiangmu','content']
    list_filter = ['athlete','date','xiangmu','mingcheng','xiangmu','jibie','nandufen','wanchengfen','zongfen']
    model_icon = 'fa fa-trophy'
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





class  ChengjiShAdmin(object):
    list_display = ['xingming','riqi','gaotong','nandufen','wanchengfen','zongfen']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','gaotong','nandufen','wanchengfen','zongfen']

    # data_charts = {
    #         "user_count": {'title': u"训练-生化", "x-field": "riqi", "y-field": ("gaotong", ), "order": ('riqi',)},
    #         # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    #     }

# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(ChengjiDate,ChengjiDateAdmin)
xadmin.site.register(ChengjiSh,ChengjiShAdmin)