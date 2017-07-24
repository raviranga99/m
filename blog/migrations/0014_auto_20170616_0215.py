# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170507_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
