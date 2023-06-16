from django.contrib import admin
from .models import PetsInfo
# Register your models here.
#直接注册模型类
#admin.site.register(Account)

#自定义显示模型类字段
#class UserAccountAdmin(admin.ModelAdmin):
    #list_display = ['id','name','password']
#注册
#admin.site.register(Account,UserAccountAdmin)


class PetsInfoAdmin(admin.ModelAdmin):
       
    list_display=[ 'pet_id', 
    'pet_name', 
    'pet_type',
    'gender', 
    
    'description',
    'level', 
    'exp',
    'uid', 
    'date', 
    'mode_type',
    'p_avatar']


admin.site.register(PetsInfo,PetsInfoAdmin)