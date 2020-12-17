from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=12)
    surname = models.CharField(max_length=12)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=96)
    email = models.CharField(max_length=20)
    type = models.CharField(max_length=8)
    active = models.BooleanField()
    own_posts = models.ArrayField(models.ObjectIdField)
    part_posts = models.ArrayField(models.ObjectIdField)
