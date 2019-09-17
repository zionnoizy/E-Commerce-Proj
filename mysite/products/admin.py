from django.contrib import admin
from .models import Product_model, Category_model


# Register your models here.
admin.site.register(Product_model)
admin.site.register(Category_model)
