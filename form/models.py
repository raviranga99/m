from django.db import models
class Mform(models.Model):
    name=models.CharField(max_length=100)
    article=models.TextField(max_length=200)