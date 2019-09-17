from django.contrib import admin
from .models import Shopping_cart_item_model, Shopping_cart_model


# Register your models here.
admin.site.register(Shopping_cart_item_model)
admin.site.register(Shopping_cart_model)
