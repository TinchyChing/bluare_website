# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0017_auto_20160723_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcontent',
            name='image',
            field=models.ImageField(default='./static/images/user.jpg', upload_to='./static/upload/post'),
        ),
    ]
