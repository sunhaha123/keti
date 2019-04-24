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
    list_display = ['xingming','riqi','leijishijian','gaotong','pizhichun','niaosudan','jisuanjimei']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','leijishijian','gaotong','pizhichun','niaosudan','jisuanjimei',]
    data_charts = {
            "user_count": {'title': u"训练（天数）-生化(睾酮)", "x-field": "leijishijian", "y-field": ("gaotong", ), "order": ('leijishijian',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
            "user_count2": {'title': u"训练（天数）-生化（皮质醇）", "x-field": "leijishijian", "y-field": ("pizhichun",), "order": ('leijishijian',)},
            "user_count3": {'title': u"训练（天数）-生化（尿素氮）", "x-field": "leijishijian", "y-field": ("niaosudan",), "order": ('leijishijian',)},
            "user_count4": {'title': u"训练（天数）-生化（肌酸激酶）", "x-field": "leijishijian", "y-field": ("jisuanjimei",), "order": ('leijishijian',)},
        # "user_count": {'title': u"训练（日期）-生化", "x-field": "riqi", "y-field": ("yichang",), "order": ('riqi',)},
        }

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
                sql = XunlianSh(
                    xingming_id=col[0],
                    riqi=str(datetime(*xldate_as_tuple(col[1], 0)))[0:10],
                    leijishijian=int(col[2]),
                    gaotong=float(col[3]),
                    pizhichun=float(col[4]),
                    niaosudan=float(col[5]),
                    jisuanjimei=float(col[6]),


                )
                sql_list.append(sql)
                XunlianSh.objects.bulk_create(sql_list)
        return super(XunlianShAdmin, self).post(request, args, kwargs)



class  XunlianCjAdmin(object):
    list_display = ['xingming','riqi','mingcheng','xiangmu','tianshu','nandufen','wanchengfen','zongfen','sbcishu','sbyuanyin']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','mingcheng','xiangmu','tianshu','nandufen','wanchengfen','zongfen','sbcishu','sbyuanyin']
    data_charts = {
            "user_count": {'title': u"训练（天数）-成绩", "x-field": "tianshu", "y-field": ("nandufen","wanchengfen","zongfen" ), "order": ('riqi',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
        }

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
                sql = XunlianCj(
                    xingming_id=col[0],
                    riqi=str(datetime(*xldate_as_tuple(col[1], 0)))[0:10],
                    mingcheng=str(col[2]),
                    xiangmu_id=col[3],
                    tianshu=int(col[4]),
                    nandufen=float(col[5]),
                    wanchengfen=float(col[6]),
                    zongfen=float(col[7]),
                    sbcishu=str(col[8]),
                    sbyuanyin=str(col[9]),


                )
                sql_list.append(sql)
                XunlianCj.objects.bulk_create(sql_list)
        return super(XunlianCjAdmin, self).post(request, args, kwargs)



class  ChengjiShAdmin(object):
    list_display = ['xingming','riqi','gaotong','pizhichun','niaosudan','jisuanjimei','nandufen','wanchengfen','zongfen']
    # search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','gaotong','pizhichun','niaosudan','jisuanjimei','nandufen','wanchengfen','zongfen']

    data_charts = {
            "user_count": {'title': u"生化(睾酮)-成绩", "x-field": "gaotong", "y-field": ("nandufen","zongfen","wanchengfen" ), "order": ('gaotong',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
        "user_count2": {'title': u"生化（皮质醇-成绩", "x-field": "pizhichun", "y-field": ("nandufen","zongfen","wanchengfen" ),
                        "order": ('pizhichun',)},
        "user_count3": {'title': u"生化（尿素氮）-成绩", "x-field": "niaosudan", "y-field": ("nandufen","zongfen","wanchengfen" ),
                        "order": ('niaosudan',)},
        "user_count4": {'title': u"生化（肌酸激酶）-成绩", "x-field": "jisuanjimei", "y-field": ("nandufen","zongfen","wanchengfen"),
                        "order": ('jisuanjimei',)},
        }

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
                sql = ChengjiSh(
                    xingming_id=col[0],
                    riqi=str(datetime(*xldate_as_tuple(col[1], 0)))[0:10],
                    gaotong=float(col[2]),
                    pizhichun=float(col[3]),
                    niaosudan=float(col[4]),
                    jisuanjimei=float(col[5]),
                    nandufen=float(col[6]),
                    wanchengfen=float(col[7]),
                    zongfen=float(col[8])

                )
                sql_list.append(sql)
                ChengjiSh.objects.bulk_create(sql_list)
        return super(ChengjiShAdmin, self).post(request, args, kwargs)




class  XunlianDateAdmin2(object):
    list_display = ['xingming','riqi','xiangmu','content']
    # search_fields = ['xingming_name',]
    list_filter = ['xingming','riqi','xiangmu','content']
    model_icon = 'fa fa-align-left'

xadmin.site.register(XunlianSh,XunlianShAdmin)
xadmin.site.register(XunlianCj,XunlianCjAdmin)
xadmin.site.register(ChengjiSh,ChengjiShAdmin)
# xadmin.site.register(XunlianDate,XunlianDateAdmin2)