from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order, DeliveryBoy, DeliveryBoy_Catlog

from django.contrib.auth import get_user_model

from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync

User = get_user_model()
@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    delivery_boy = DeliveryBoy(user=instance)
    delivery_boy.save()
    catlog = DeliveryBoy_Catlog(user=instance)
    catlog.save()


@receiver(post_save, sender=Order)
def order_placed(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    room_name = 'room_name'
    print('at rpm',room_name)
    print(created)
    if created:
        async_to_sync(channel_layer.group_send)(room_name, 
        {
                'type': 'send_status_of_order',
                'status_type':'order placed',
                'order_id': instance.id,
                'delevered_by':instance.delevered_by.id if hasattr(instance,'delivery_by') else -1 ,
                'status' : instance.status
                # 'delevered_by':instance.delevered_by               

                }
                )
    else:
        async_to_sync(channel_layer.group_send)(room_name, 
        {
                'type': 'send_status_of_order',
                'status_type': 'order modified',
                'delevered_by':instance.delevered_by.id if hasattr(instance,'delivery_by') else -1 ,
                

                'order_id': instance.id,
                'status' : instance.status
                # 'delevered_by':instance.delevered_by               

                }
                )
