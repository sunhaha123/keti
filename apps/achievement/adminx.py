# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import ChengjiDate,Tubiao1
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
from django.utils.safestring import mark_safe

class  ChengjiDateAdmin(object):
    list_display = ['athlete','date','xiangmu','mingcheng','jibie','nandufen','wanchengfen','zongfen']
    # search_fields = ['xingming_id','riqi','xiangmu','content']
    list_filter = ['athlete','date','xiangmu','mingcheng','jibie','nandufen','wanchengfen','zongfen']
    model_icon = 'fa fa-trophy'
    import_excel=True
    data_charts = {
            "user_count": {'title': u"难度分", "x-field": "date", "y-field": ("nandufen", ), "order": ('date',)},
            "user_count2": {'title': u"完成分", "x-field": "date", "y-field": ("wanchengfen",), "order": ('date',)},
            "user_count3": {'title': u"总分", "x-field": "date", "y-field": ("zongfen",), "order": ('date',)},
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

class Tubiao1Admin(object):
        list_display = ('title', 'image_data','introduce')
        readonly_fields = ('image_data',)  # 必须加这行 否则访问编辑页面会报错
        export_excel = False
        # say_hello = False
        # list_export = ('xlsx')
        # list_export_fields = None

        def image_data(self, obj):
            return mark_safe(u'<img src="%s" width="500px" />' % obj.image.url)

        # 页面显示的字段名称
        image_data.short_description = u'饼图图片'





# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(ChengjiDate,ChengjiDateAdmin)
xadmin.site.register(Tubiao1,Tubiao1Admin)