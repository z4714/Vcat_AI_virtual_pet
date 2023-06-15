from django.db import models
from login.models import Account
# Create your models here.



class PetsInfo(models.Model):
    pet_id = models.IntegerField(primary_key=True,verbose_name='宠物ID',default=0)
    pet_name = models.CharField(max_length=24,verbose_name='宠物名称')
    pet_type = models.CharField(max_length=254,verbose_name='宠物类型')
    level = models.IntegerField(verbose_name='等级', default=0)
    exp  = models.IntegerField(verbose_name='经验值',default=0)
    uid = models.ForeignKey(Account,default=0,on_delete=models.SET_DEFAULT)
    date = models.DateField(verbose_name='生成日期',null=False)
    mode_type = models.CharField(max_length=254,verbose_name='模型类型',blank=True)


    class Meta:
        #默认生成的表名：
        db_table = 'pets_info'
        managed = True
        #表的说明信息
        verbose_name = 'pets infomration by pet_id'
        verbose_name_plural = '宠物仓'
    
    def __str__(self):
        return self.uname