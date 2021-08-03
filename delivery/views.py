from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response 

from .serializers import OrderSerializer, UserSerializer
from .models import Order


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class=OrderSerializer
 

class GetUserDetails(APIView):
     def get(self, request, format=None):
         print(request.user)
         serializer = UserSerializer(request.user)
         return Response(serializer.data)