# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSystem', '0013_auto_20160722_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birthday',
            field=models.TextField(default='2016/07/23', max_length=100),
        ),
    ]
