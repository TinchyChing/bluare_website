# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FriendSystem', '0003_auto_20160716_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmeaasge',
            name='meaasge',
            field=models.TextField(default=''),
        ),
    ]
