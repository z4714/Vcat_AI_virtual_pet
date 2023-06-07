from django.contrib import admin
from .models import Account,Email,UserInfo
# Register your models here.
#直接注册模型类
#admin.site.register(Account)

#自定义显示模型类字段
#class UserAccountAdmin(admin.ModelAdmin):
    #list_display = ['id','name','password']
#注册
#admin.site.register(Account,UserAccountAdmin)
class AccountAdmin(admin.ModelAdmin):
    list_display=['uid','uname']

class EmailAdmin(admin.ModelAdmin):
    list_display=['uid','email']

class UserInfoAdmin(admin.ModelAdmin):
    list_display=['uname','pwd','nickname','gender','birth','date','photo']

admin.site.register(Account,AccountAdmin)
admin.site.register(Email,EmailAdmin)
admin.site.register(UserInfo,UserInfoAdmin)