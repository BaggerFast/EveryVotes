from djongo import models


class Post(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    created_at = models.DateField()
    publish_at = models.DateField()
    finish_at = models.DateField()
    visible = models.BooleanField()


class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=12)
    surname = models.CharField(max_length=12)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=96)
    email = models.CharField(max_length=20)
    type = models.CharField(max_length=8)
    active = models.BooleanField()
    posts = models.ManyToManyField(Post)
