# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design6', '0008_auto_20180126_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='user/%Y/%m/%d'),
        ),
    ]
