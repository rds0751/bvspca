# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('animals', '0016_auto_20171229_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalCountSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cats_adopted', models.PositiveIntegerField()),
                ('cats_rescued', models.PositiveIntegerField()),
                ('dogs_adopted', models.PositiveIntegerField()),
                ('dogs_rescued', models.PositiveIntegerField()),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]