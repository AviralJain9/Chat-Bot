from django.urls import path 
from . import views

app_name = 'orders'

urlpatterns = [
    path('add/', views.add, name = 'add'),
    path('pyconfirmation/', views.payment_confirmation, name = 'payment_confirmation'),
    path('userorders/', views.user_orders, name = 'user_orders'),
]