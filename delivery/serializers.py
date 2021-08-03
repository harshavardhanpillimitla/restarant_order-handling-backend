from rest_framework import serializers
from .models import Order,DeliveryBoy
from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField


User = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    blocked = SerializerMethodField()
    class Meta:
        model = User
        fields =  ['id', 'username','blocked']

    def get_blocked(self, obj):
        db = DeliveryBoy.objects.get(user=obj.id)
        return db.blocked