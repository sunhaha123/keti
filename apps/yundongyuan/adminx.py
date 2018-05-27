# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import Athlete
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple

class  AthleteAdmin(object):
    list_display = ['id','name','gender','coach', 'birthday','join_date','character','achievement','is_actice']
    # search_fields = ['id','name','gender', 'birthday','join_date','is_actice']
    list_filter = ['id','name','gender','coach', 'birthday','join_date','character','achievement','is_actice']
    model_icon = 'fa fa-tags'
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
                    sql = Athlete(
                        name=col[0],
                        gender=col[1],
                        birthday=str(datetime(*xldate_as_tuple(col[2], 0)))[0:10],
                        coach_id=col[3],
                        join_date=str(datetime(*xldate_as_tuple(col[4], 0)))[0:10],
                        character=col[5],
                        achievement=col[6],
                        is_actice=col[7]
                    )
                    sql_list.append(sql)
                Athlete.objects.bulk_create(sql_list)
            return super(AthleteAdmin, self).post(request, args, kwargs)


# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Athlete,AthleteAdmin)