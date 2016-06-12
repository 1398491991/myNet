# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='joke',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(verbose_name='\u66f4\u6539\u65f6\u95f4')),
                ('title', models.CharField(max_length=150, verbose_name='\u7b11\u8bdd\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('img_uuid', models.CharField(max_length=50, null=True, verbose_name='\u56fe\u7247UUID')),
                ('create_joke_user_id', models.ForeignKey(related_query_name=b'create_joke_user_id', to='user_info.user_info')),
            ],
            options={
                'db_table': 'joke',
            },
        ),
        migrations.CreateModel(
            name='joke_operating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(verbose_name='\u66f4\u6539\u65f6\u95f4')),
                ('operating_type', models.SmallIntegerField(verbose_name='\u64cd\u4f5c\u7c7b\u578b')),
                ('operating_type_china', models.CharField(max_length=10, verbose_name='\u64cd\u4f5c\u7c7b\u578b\u2014\u2014\u4e2d\u6587')),
                ('operating_text', models.CharField(max_length=250, verbose_name='\u5185\u5bb9')),
                ('joke_id', models.ForeignKey(related_query_name=b'joke_id', to='joke.joke')),
                ('operating_joke_user_id', models.ForeignKey(related_query_name=b'operating_joke_user_id', to='user_info.user_info')),
            ],
            options={
                'db_table': 'joke_operating',
            },
        ),
    ]
