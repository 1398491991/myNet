# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='create_joke_user_id',
            field=models.ForeignKey(related_name='create_joke_user_id', to='user_info.user_info'),
        ),
        migrations.AlterField(
            model_name='joke_operating',
            name='joke_id',
            field=models.ForeignKey(related_name='joke_id', to='joke.joke'),
        ),
        migrations.AlterField(
            model_name='joke_operating',
            name='operating_joke_user_id',
            field=models.ForeignKey(related_name='operating_joke_user_id', to='user_info.user_info'),
        ),
    ]
