from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Voting(models.Model):
    """
    Model Voting

    :param author: creator of Voting
    :param title: title of Voting
    :param description: description of Voting
    :param closed: closed status of Voting (default false)
    :param date_created: creation date/time of the voting (created automatically when creating)
    """

    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    closed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)


class VoteVariant(models.Model):
    """
    Model VoteVariant

    :param voting: the Voting to which the VoteVariant belongs
    :param title: title of VoteVariant
    """

    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)


class UserVote(models.Model):
    """
    Model UserVote

    Which voice did the user choose in the voting

    :param vote_variant: selected VoteVariant of user
    :param user: the user who voted
    """
    vote_variant = models.ForeignKey(to=VoteVariant, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
