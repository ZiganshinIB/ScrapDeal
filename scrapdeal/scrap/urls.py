from django.urls import path, include
from .views import account_notifications, account

app_name = 'scrap'

urlpatterns = [
    path('', account, name='account'),
    path('notifications', account_notifications, name='account-notifications'),
]
