# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 09:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160515_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 15, 9, 46, 52, 985994, tzinfo=utc)),
        ),
    ]
