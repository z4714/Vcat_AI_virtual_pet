from django.db import models
from login.models import Account
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.



class PetsInfo(models.Model):
    pet_id = models.IntegerField(primary_key=True,verbose_name='宠物ID',default=0)
    pet_name = models.CharField(max_length=24,verbose_name='宠物名称')
    pet_type = models.CharField(max_length=254,verbose_name='宠物类型')
    gender = models.CharField(max_length=12,verbose_name='宠物性别',blank=True)
    
    level = models.IntegerField(verbose_name='等级', default=0)
    exp  = models.IntegerField(verbose_name='经验值',default=0)
    uid = models.ForeignKey(Account,default=0,on_delete=models.SET_DEFAULT)
    date = models.DateField(verbose_name='生成日期')
    mode_type = models.CharField(max_length=254,verbose_name='模型类型',blank=True)
    p_avatar =models.TextField(verbose_name='宠物图像',null=True)

    class Meta:
        #默认生成的表名：
        db_table = 'pets_info'
        managed = True
        #表的说明信息
        verbose_name = 'pets infomration by pet_id'
        verbose_name_plural = '宠物仓'
    
    def __str__(self):
        return self.uname

@receiver(pre_save, sender=PetsInfo)
def increment_pet_id(sender, instance, **kwargs):
    if instance.pet_id == 0:
        max_pet_id = PetsInfo.objects.aggregate(models.Max('pet_id'))['pet_id__max']
        instance.pet_id = max_pet_id + 1 if max_pet_id else 1