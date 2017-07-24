# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title=models.CharField(max_length=120)
