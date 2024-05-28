# Generated by Django 5.0.6 on 2024-05-23 14:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_remove_cart_products_remove_cart_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
