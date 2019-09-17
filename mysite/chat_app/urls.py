# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.chat, name='chat'),
    path('j/son/', views.rest_chat, name='rest_chat'),
]
