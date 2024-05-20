from django.core.management.base import BaseCommand
from user_management.models import CustomUser

class Command(BaseCommand):
    help = 'Create a new superuser'

    def handle(self, *args, **kwargs):
        email = input('Email: ')
        password = input('Password: ')
        if not CustomUser.objects.filter(email=email).exists():
            CustomUser.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.ERROR('User with this email already exists'))