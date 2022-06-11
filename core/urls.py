from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'apartments', views.ApartmentViewSet)
router.register(r'apartment_media', views.ApartmentMediaViewset)
router.register(r'reservations', views.ReservationsViewSet)
router.register(r'cars', views.CarsViewSet)
router.register(r'car_media', views.CarMediaViewSet)
router.register(r'host', views.HostViewSet)
router.register(r'host_profile', views.HostProfileViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.RentalView.as_view(), name='rentals'),
    path('get_started/', views.GetStartedView.as_view(), name='get_started'),
    path('become_a_host/', views.BecomeAHostView.as_view(), name='host'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('routers', include(router.urls)),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
  
]