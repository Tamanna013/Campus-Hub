from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/v1/auth/', include('auth_app.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/clubs/', include('clubs.urls')),
    path('api/v1/events/', include('events.urls')),
    path('api/v1/resources/', include('resources.urls')),
    path('api/v1/bookings/', include('bookings.urls')),
    path('api/v1/chats/', include('chats.urls')),
    path('api/v1/notifications/', include('notifications.urls')),
    path('api/v1/analytics/', include('analytics.urls')),
    path('api/v1/files/', include('files.urls')),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)