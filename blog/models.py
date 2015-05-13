from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.TextField()
    body = models.TextField()
    status = models.IntegerField(default=1)
    gmt_create = models.DateTimeField(default=datetime.utcnow)
    gmt_modify = models.DateTimeField(default=datetime.utcnow)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title
