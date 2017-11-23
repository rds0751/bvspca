# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 19:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0008_animalspage_species'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='surrender_date',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
            preserve_default=False,
        ),
    ]