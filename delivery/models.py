from django.db import models

from django.contrib.auth import get_user_model


User =  get_user_model()

# Create your models here.
class DeliveryBoy(models.Model):
    active = models.BooleanField(default=True)
    user =  models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='delivery_boy')
    
    blocked = models.BooleanField(default=False)
    # delivery_catlog = models.ForeignKey(DeliveryBoy_Catlog, on_delete=models.CASCADE)

class amounts(models.Model):
    bonous = models.IntegerField(default=0)
    penality = models.IntegerField(default=1)
    


class Order(models.Model):
    STATUS_ORDER_PLACED = 'OP'
    STATUS_ORDER_DELIVERED = 'OD'
    STATUS_ORDER_UN_DELIVERED = 'UD'
    STATUS_ORDER_DELIVERING = 'DL'

    DELIVERY_STATUS  = (
        (STATUS_ORDER_DELIVERED, 'order delivered'),
        (STATUS_ORDER_PLACED, 'order placed'),
        (STATUS_ORDER_UN_DELIVERED, 'order undelivered'),
        (STATUS_ORDER_DELIVERING, 'order delivereding')
    )

    status = models.CharField(max_length=2, choices=DELIVERY_STATUS, default=STATUS_ORDER_PLACED)
    delevered_by = models.ForeignKey(DeliveryBoy, on_delete=models.DO_NOTHING , null=True, blank=True)
    reason_of_undelivered = models.CharField(max_length=250, null=True, blank=True)

class DeliveryBoy_Catlog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    month = models.DateField(auto_now=True)
    items_delivered = models.IntegerField(default=0)
    penality_of_the_month = models.IntegerField(default=0)
    bonous = models.IntegerField(default=0)
    items_undelivered = models.IntegerField(default=0)

    salary = models.IntegerField(default=0)

    
    