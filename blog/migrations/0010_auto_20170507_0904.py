# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170507_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='h',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='w',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, height_field=b'h', null=True, upload_to=b'', width_field=b'w'),
        ),
    ]
