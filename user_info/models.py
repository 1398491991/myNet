#coding=utf-8
from django.db import models

# Create your models here.
class user_info(models.Model):
    create_time=models.DateTimeField(verbose_name=u'创建时间',null=False)
    update_time=models.DateTimeField(verbose_name=u'修改时间',null=False)
    user_name=models.CharField(verbose_name=u'账号',max_length=15,unique=True,null=False)
    user_password=models.CharField(verbose_name=u'密码',max_length=25,null=False)
    # birthday=models.DateField(verbose_name=u'生日',null=True)
    # email=models.CharField(verbose_name=u'邮箱',max_length=30,unique=True,null=True)
    # city=models.CharField(verbose_name=u'城市',max_length=10,null=False)
    class Meta:
        db_table = 'user_info'
    def __unicode__(self):
        return self.user_name