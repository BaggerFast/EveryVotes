from djongo import models


class Post(models.Model):
    id = models.ObjectIdField()
    author = models.IntegerField()
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    publish_at = models.DateTimeField()
    finish_at = models.DateTimeField()
    visible = models.BooleanField()
