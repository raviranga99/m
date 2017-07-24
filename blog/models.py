
from django.db import models
from django.utils import timezone

class Tag(models.Model):
    slug=models.SlugField(unique=True,max_length=50)
    def __str__(self):
        return self.slug


class Post(models.Model):
    title=models.CharField(max_length=50,default="")
    slug=models.SlugField(unique=True,default="")
    body=models.TextField(default="body")
    img=models.ImageField(null=True,blank=True,width_field="w",height_field="h")
    h=models.IntegerField(default=0)
    w=models.IntegerField(default=0)
    create=models.DateTimeField(default=timezone.now)
    tag=models.ManyToManyField(Tag)
    published=models.BooleanField(default=True)
    def __str__(self):
        return self.title


