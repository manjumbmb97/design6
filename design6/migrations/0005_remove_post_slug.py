# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 02:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design6', '0004_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
