"""
Custom command for django in console
"""

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Custom command: auto_migrate - unites commands makemigrations && migrate
    """

    help = 'Unites commands makemigrations && migrate'

    def handle(self, *args, **options):
        call_command('makemigrations')
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS(f'SUCCESS'))

