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
        if self.publish_at < timezone.now() < self.finish_at:
            self.visible = True
            self.save()
        elif timezone.now() < self.publish_at:
            self.visible = False
            self.save()
        elif self.finish_at < timezone.now():
            self.closed = True
            self.save()

    def __repr__(self):
        return self.author


class VoteVariant(models.Model):
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)


class VoteFact(models.Model):
    variant = models.ForeignKey(to=VoteVariant, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
