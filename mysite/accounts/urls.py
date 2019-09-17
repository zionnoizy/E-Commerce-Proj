from django.urls import path, include
from django.contrib.auth import views as adminviews
from . import views

urlpatterns = [
    path('login/', adminviews.LoginView.as_view()),
    path('register/', views.register),
]
