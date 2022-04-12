"""
Custom command for django in console
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Custom command: create_admin - for quick and easy creation of a superuser in development
    """

    username = 'root'
    password = 'root'
    email = '1@abc.net'

    def handle(self, *args, **options):
        get_user_model().objects.create_superuser(self.username, self.email, self.password)
        self.stdout.write(self.style.SUCCESS(f'Super user {self.username} successfully created!'))
