from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Voting(models.Model):
    """
    Model Voting

    :param author: creator of Voting
    :param title: title of Voting
    :param description: description of Voting
    :param closed: closed status of Voting (default false)
    :param date_created: creation date/time of the voting (created automatically when creating)
    """

    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=25, verbose_name='Заголовок')
    description = models.CharField(max_length=100, verbose_name='Описание')
    closed = models.BooleanField(default=False, verbose_name='Закрыто')
    date_created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'

    def __str__(self):
        return f'{self.title}({self.id})'


class VoteVariant(models.Model):
    """
    Model VoteVariant

    :param voting: the Voting to which the VoteVariant belongs
    :param title: title of VoteVariant
    """

    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE, verbose_name='Голосование')
    title = models.CharField(max_length=25, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Вариант голосования'
        verbose_name_plural = 'Варианты голосования'

    def __str__(self):
        return f'{self.voting}: {self.title}'


class UserVote(models.Model):
    """
    Model UserVote

    Which voice did the user choose in the voting

    :param vote_variant: selected VoteVariant of user :type int
    :param user: the user who voted
    """
    vote_variant = models.ForeignKey(to=VoteVariant, on_delete=models.CASCADE, verbose_name='Вариант голосования')
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, verbose_name='Проголосовавший пользователь')

    class Meta:
        verbose_name = 'Голос пользователя'
        verbose_name_plural = 'Голоса пользователей'
