"""
URL configuration for Bank_django project.
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # app urls
    path('', include('app.urls')),
]

# For media files (images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)