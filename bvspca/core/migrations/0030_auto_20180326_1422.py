# Generated by Django 2.0.3 on 2018-03-26 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('core', '0029_auto_20180321_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentindexpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='This image should be exactly 1600px wide and 560px high.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='page banner image'),
        ),
        migrations.AddField(
            model_name='contentindexpage',
            name='menu_item_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='menu image'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='This image should be exactly 1600px wide and 560px high.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='page banner image'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='menu_item_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='menu image'),
        ),
        migrations.AddField(
            model_name='supporterspage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='This image should be exactly 1600px wide and 560px high.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='page banner image'),
        ),
        migrations.AddField(
            model_name='supporterspage',
            name='menu_item_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='menu image'),
        ),
        migrations.AddField(
            model_name='teampage',
            name='banner_image',
            field=models.ForeignKey(blank=True, help_text='This image should be exactly 1600px wide and 560px high.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='page banner image'),
        ),
        migrations.AddField(
            model_name='teampage',
            name='menu_item_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='menu image'),
        ),
    ]
