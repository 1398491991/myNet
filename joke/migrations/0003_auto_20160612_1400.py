# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0002_auto_20160612_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='create_joke_user_id',
            field=models.ForeignKey(to='user_info.user_info'),
        ),
        migrations.AlterField(
            model_name='joke_operating',
            name='joke_id',
            field=models.ForeignKey(to='joke.joke'),
        ),
        migrations.AlterField(
            model_name='joke_operating',
            name='operating_joke_user_id',
            field=models.ForeignKey(to='user_info.user_info'),
        ),
    ]
