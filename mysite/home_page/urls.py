from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sort/<str:category>/', views.category, name='category'),
    path('discussion_board/', views.discussion_board, name='discussion_board'),
    path('employee/', views.employee, name='employee')
]
