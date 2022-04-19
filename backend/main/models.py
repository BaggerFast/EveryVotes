from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text='Требуется не более 20 знаков. Также можно использовать буквы, цифры и @/./+/-/_',
    )
    # email = models.EmailField(
    #     verbose_name='email address',
    #     max_length=255,
    #     unique=True,
    # )

    def __str__(self):
        return self.username
