# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170507_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, height_field=100, null=True, upload_to=b'', width_field=100),
        ),
    ]
