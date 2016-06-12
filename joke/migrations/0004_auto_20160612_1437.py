# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0003_auto_20160612_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke_operating',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 12, 14, 37, 29, 885000), verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='joke_operating',
            name='state',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='joke_operating',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 12, 14, 37, 29, 886000), verbose_name='\u66f4\u6539\u65f6\u95f4'),
        ),
    ]
