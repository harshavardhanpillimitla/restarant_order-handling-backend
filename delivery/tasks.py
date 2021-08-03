from celery import shared_task
from delivery.models import DeliveryBoy
from delivery.models import DeliveryBoy_Catlog, amounts
from django.db.models  import F


@shared_task(ignore_result=True)
def deactivate_user(user_ids):
    user_obj = DeliveryBoy.objects.filter(user__in=user_ids).update(blocked=True)


@shared_task(ignore_result=True)
def caliculate_salaries(): 
    amount = amounts.objects.last()
    print(amount)
    catlog = DeliveryBoy_Catlog.objects.all().update(salary=F('items_delivered')+amount.bonous-F('items_undelivered')-amount.penality)
