from django.db import models
from .models  import DeliveryBoy, DeliveryBoy_Catlog

class DeliveryBoyModelManager(models.Manager):
    def create(self, user):
        delivery_boy = DeliveryBoy(user=user)
        delivery_boy.save()
        catlog = DeliveryBoy_Catlog(user=user)
        catlog.save()
        return delivery_boy
