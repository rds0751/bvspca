# Generated by Django 2.0.4 on 2018-08-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0025_animal_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalspage',
            name='show_newsletter_signup',
            field=models.BooleanField(default=True),
        ),
    ]