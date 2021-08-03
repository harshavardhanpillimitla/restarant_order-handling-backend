from django.contrib import admin

from .models import Order,DeliveryBoy_Catlog,DeliveryBoy,amounts
# Register your models here.
admin.site.register(Order)
admin.site.register(DeliveryBoy_Catlog)
admin.site.register(DeliveryBoy)
admin.site.register(amounts)
