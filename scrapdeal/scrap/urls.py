from django.urls import path, include
from .views import account_notifications, account, get_my_orders, get_orders

app_name = 'scrap'

urlpatterns = [
    path('', account, name='account'),
    path('notifications', account_notifications, name='account-notifications'),
    path('my-orders', get_my_orders, name='my-orders'),
    path('orders', get_orders, name="orders"),
]
