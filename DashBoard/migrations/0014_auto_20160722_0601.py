# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0013_auto_20160719_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcontent',
            name='blog_type',
            field=models.CharField(default='游记', max_length=5),
        ),
        migrations.AddField(
            model_name='postcontent',
            name='content_type',
            field=models.CharField(default='动态', max_length=5),
        ),
        migrations.AddField(
            model_name='postcontent',
            name='photo_type',
            field=models.CharField(default='游记', max_length=5),
        ),
    ]
