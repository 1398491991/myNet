#coding=utf8
from django.db import models
from user_info.models import user_info

# Create your models here.
class joke(models.Model):
    state=models.IntegerField(verbose_name=u'状态',null=False)
    create_time=models.DateTimeField(verbose_name=u'创建时间',null=False)
    update_time=models.DateTimeField(verbose_name=u'更改时间',null=False)
    title=models.CharField(verbose_name=u'笑话标题',null=False,max_length=150)
    content=models.TextField(verbose_name=u'内容',null=False,)
    img_uuid=models.CharField(verbose_name=u'图片UUID',null=True,max_length=50)
    create_joke_user_id=models.ForeignKey(user_info)
    class Meta:
        db_table = 'joke'


class joke_operating(models.Model):
    state=models.IntegerField(verbose_name=u'状态',null=False,default=0)
    create_time=models.DateTimeField(verbose_name=u'创建时间',null=False,)
    update_time=models.DateTimeField(verbose_name=u'更改时间',null=False,)
    joke_id=models.ForeignKey(joke)
    operating_joke_user_id=models.ForeignKey(user_info)
    operating_type=models.SmallIntegerField(verbose_name=u'操作类型',null=False)
    operating_type_china=models.CharField(verbose_name=u'操作类型——中文',null=False,max_length=10)
    operating_text=models.CharField(verbose_name=u'内容',null=False,max_length=250)
    class Meta:
        db_table='joke_operating'

