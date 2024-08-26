
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scrap.urls', namespace='scrap'),),
    path('api/', include('account.api_urls', namespace='api_account'),),
    path('api/', include('scrap.api_urls', namespace='api_scrap'),),
    path('account/', include('account.urls', namespace='account'),),
]

# media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
