# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FriendSystem', '0008_auto_20160717_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='email',
            field=models.EmailField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='friends',
            name='friends',
            field=models.TextField(default='[]'),
        ),
    ]