from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.datetime_safe import datetime
from djongo import models


class Voting(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    publish_at = models.DateTimeField()
    finish_at = models.DateTimeField()
    rating = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)

    def check_closed(self):
        return self.finish_at > timezone.now()

    def __repr__(self):
        return self.finish_at


class VoteVariant(models.Model):
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)

