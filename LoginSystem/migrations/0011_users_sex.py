# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSystem', '0010_users_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='sex',
            field=models.CharField(default='中性', max_length=1),
        ),
    ]