# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FriendSystem', '0011_addmessage_disagree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmessage',
            name='disagree',
            field=models.TextField(default='[]'),
        ),
    ]
