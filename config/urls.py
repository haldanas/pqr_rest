from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

# urlpatterns = [
#     # Django Admin
    
#     path(settings.ADMIN_URL, admin.site.urls),

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path

urlpatterns = [
    path('',include(('apipqr.users.urls','users'), namespace='users')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
