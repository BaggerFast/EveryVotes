from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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

    def check_settings(self):
        if self.finish_at < timezone.now():
            return False
        else:
            return True


class VoteVariant(models.Model):
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)

    def remake(self, data):
        self.description = data
        self.save()


class VoteFact(models.Model):
    variant = models.ForeignKey(to=VoteVariant, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
