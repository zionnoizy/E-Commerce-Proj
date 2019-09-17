from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_out, name='check_out'),
    path('success/', views.success, name='success'),
]
