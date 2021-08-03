from django.core.management.base import BaseCommand, CommandError
from delivery.models import DeliveryBoy_Catlog

from delivery.tasks import caliculate_salaries

class Command(BaseCommand):
    help = "caliculate salaries"     
    
        
    def handle(self, *args, **options):
        
        caliculate_salaries.delay()
        