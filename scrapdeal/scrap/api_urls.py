from rest_framework import routers
from django.urls import path, include
from .api_views import *

app_name = 'api_scrap'
router = routers.SimpleRouter()
router.register(r'order', OrderViewSet)


urlpatterns = [
    path('',include(router.urls)),
]