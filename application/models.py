from django.contrib.auth.models import User
from django.utils import timezone
from djongo import models


class Voting(models.Model):
    id = models.ObjectIdField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    publish_at = models.DateTimeField()
    finish_at = models.DateTimeField()
    rating = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
