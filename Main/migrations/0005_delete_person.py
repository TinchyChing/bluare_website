# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-09 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_remove_person_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]