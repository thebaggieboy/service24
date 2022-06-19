
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('allauth.urls')),
    path('', views.IndexView.as_view(), name='home'),
    path('explore/', include('core.urls')),
    path('host/', include('hosts.urls')),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
