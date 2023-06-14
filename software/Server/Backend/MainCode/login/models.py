from django.db import models


# Create your models here.

class Account(models.Model):
    uid = models.AutoField(primary_key=True,verbose_name='用户ID')
    uname = models.CharField(max_length=30,verbose_name='用户名',default='')
    class Meta:
        #默认生成的表名：
        db_table = 'account'
        managed = True
        #表的说明信息
        verbose_name = 'Account:uid-uname'
        verbose_name_plural = '用户名'
    def __str__(self) -> str:
        return super().__str__()


class Email(models.Model):
    uid = models.AutoField(primary_key=True,verbose_name='用户ID')
    email = models.EmailField(max_length=30,verbose_name='邮箱')
    class Meta:
        #默认生成的表名：
        db_table = 'email'
        managed = True
        #表的说明信息
        verbose_name = 'Email:uid-email'
        verbose_name_plural = '用户邮箱'
    def __str__(self):
        return self.email

class UserInfo(models.Model):


    uname = models.CharField(max_length=30,verbose_name='用户名')
    pwd = models.CharField(max_length=24,verbose_name='密码')
    nickname = models.CharField(max_length=30, verbose_name='昵称', blank=True)
    gender  = models.CharField(max_length=30, verbose_name='性别',null=True)
    birth = models.DateField(verbose_name='出生日期',null=True)
    date = models.DateField(verbose_name='注册日期',null=False)
    avatar = models.TextField(verbose_name='用户头像',null=True)
    #def save(self, *args, **kwargs):
        #if not self.nickname:
            #self.nickname = self.uname
            #super().save(*args, **kwargs)


    class Meta:
        #默认生成的表名：
        db_table = 'user_info'
        managed = True
        #表的说明信息
        verbose_name = 'user infomration : uname'
        verbose_name_plural = '用户资料'
    
    def __str__(self):
        return self.uname