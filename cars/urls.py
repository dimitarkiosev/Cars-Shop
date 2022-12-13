from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cars import accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('cars.accounts.urls')),
    path('cars/', include('cars.car.urls')),
    path('', include('cars.core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)