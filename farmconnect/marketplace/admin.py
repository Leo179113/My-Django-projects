from django.contrib import admin
from .models import CartItem, CustomUser, Product, Order, Message

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(CartItem)
