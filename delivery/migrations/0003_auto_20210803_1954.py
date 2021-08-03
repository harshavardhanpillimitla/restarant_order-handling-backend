# Generated by Django 3.2.6 on 2021-08-03 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0002_alter_order_delevered_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryboy',
            name='penality_of_the_month',
        ),
        migrations.AddField(
            model_name='deliveryboy_catlog',
            name='penality_of_the_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deliveryboy_catlog',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('OD', 'order delivered'), ('OP', 'order placed'), ('UD', 'order undelivered'), ('DL', 'order delivereding')], default='OP', max_length=2),
        ),
    ]