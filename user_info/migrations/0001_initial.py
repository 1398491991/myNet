# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('user_name', models.CharField(unique=True, max_length=15, verbose_name='\u8d26\u53f7')),
                ('user_password', models.CharField(max_length=25, verbose_name='\u5bc6\u7801')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
