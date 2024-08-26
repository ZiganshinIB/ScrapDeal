from rest_framework import routers
from django.urls import path, include, re_path
from .api_views import *

app_name = 'api_account'

router = routers.SimpleRouter()
router.register(r'workshop', WorkShopAPIViewSet)
router.register(r'position', PositionAPIViewSet)
router.register(r'profile', ProfileAPIViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('', include('djoser.urls.authtoken')),
]