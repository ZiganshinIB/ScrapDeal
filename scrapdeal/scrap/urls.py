from django.urls import path, include
from .views import index

app_name = 'scrap'

urlpatterns = [
    path('', index, name='index'),
]
