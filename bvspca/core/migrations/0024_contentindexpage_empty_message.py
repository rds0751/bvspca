# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-25 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20180125_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentindexpage',
            name='empty_message',
            field=models.CharField(default='', max_length=200),
        ),
    ]
