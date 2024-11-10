from django.urls import path, include
from .views import index, account_notifications

app_name = 'scrap'

urlpatterns = [
    path('', index, name='account'),
]
