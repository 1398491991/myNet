# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0004_auto_20160612_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke_operating',
            name='create_time',
            field=models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='joke_operating',
            name='update_time',
            field=models.DateTimeField(verbose_name='\u66f4\u6539\u65f6\u95f4'),
        ),
    ]
