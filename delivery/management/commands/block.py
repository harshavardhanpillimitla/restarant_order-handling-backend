from django.core.management.base import BaseCommand, CommandError
from delivery.tasks import deactivate_user
class Command(BaseCommand):
    help = "deactivate / block users"     
    def add_arguments(self, parser):
        parser.add_argument('users', type=str) 
        
    def handle(self, *args, **options):
        users = [int(x) for x in options['users'][1:-1].split(',')]
        deactivate_user.delay(users)