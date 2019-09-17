from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.rest_all_products, name='rest_all_products'),
    path('<str:product_id>/', views.products_detail, name='products_detail'),

]
