import asyncio
import json
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

# from chat.redis_util import user_active_status,create_personal_chat,get_active_users,create_video_call_request,send_video_call_reject,send_video_call_accept
# from chat.consumerrequest_types.py import message_request_types
from delivery.models import Order, DeliveryBoy_Catlog, DeliveryBoy


User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name
        print(self.scope)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print('oooooooo')
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        print('ended')

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type_of_msg = text_data_json.get('type',None)
        order_modified_ref = {
            'order accepted':Order.STATUS_ORDER_DELIVERING,
            'order delivered':Order.STATUS_ORDER_DELIVERED,
            'order declined':Order.STATUS_ORDER_UN_DELIVERED

        }
        print(text_data_json)
        
        order_id = text_data_json.get('order_id')
        user_id = text_data_json.get('user_id')
        # 
        await self.change_catlog(user_id,order_id ,type_of_msg)
        instance = await self.modify_order(user_id,order_id ,order_modified_ref.get(type_of_msg,None))
        print('yelo pulelo')
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_status_of_order',
                'status_type': 'order modified',
                'delevered_by':instance.delevered_by.id if hasattr(instance,'delivery_by') else -1 ,
                'order_id': instance.id,
                'status' : instance.status

                
            }
        )
        
    #  new order arrived
    #  received order accepted 
    async def send_status_of_order(self, event):
        print('[[[')
        await self.send(text_data=json.dumps({
            'status_type':event['status_type'],
            'status':event['status'],
            'delevered_by':event['delevered_by'],
            'order_id':event['order_id']


        }))


    #     }))
    @database_sync_to_async
    def change_catlog(self, user_id, order_id,status=None):
        user = User.objects.get(id=user_id)
        catlog = DeliveryBoy_Catlog.objects.filter(user=user)
        if catlog:

            if status == 'order delivered':
                catlog[0].items_delivered += 1
            elif status == 'order declined' :
                catlog[0].items_undelivered += 1
            catlog[0].save()
            

        
    @database_sync_to_async
    def modify_order(self, user_id, order_id,status=None): 
        print(type(order_id))
        d_user = DeliveryBoy.objects.get(id=user_id)

        order = Order.objects.filter(id=order_id)   
        if order:
            order[0].status = status
            if not order[0].delevered_by:
                order[0].delevered_by = d_user
            order[0].save()
            return order[0]
  
