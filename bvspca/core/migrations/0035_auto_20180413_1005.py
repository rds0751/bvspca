# Generated by Django 2.0.4 on 2018-04-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20180412_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactformpage',
            old_name='intro',
            new_name='column_1',
        ),
    ]