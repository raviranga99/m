# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170507_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, height_field=b'h', null=True, upload_to=b'media', width_field=b'w'),
        ),
    ]
