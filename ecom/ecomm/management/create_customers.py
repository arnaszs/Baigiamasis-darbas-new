from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ecomm.models import Customer


class Command(BaseCommand):
    help = 'Create customer objects for existing users'

    def handle(self, *args, **options):
        users = User.objects.all()

        for user in users:
            Customer.objects.create(user=user)
