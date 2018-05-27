# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import Athlete
#

class  AthleteAdmin(object):
    list_display = ['id','name','gender', ]
    search_fields = ['id','name','gender',]
    list_filter = ['id','name','gender',]



# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Athlete,AthletesAdmin)