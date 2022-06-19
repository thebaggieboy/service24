from rest_framework import routers
from .viewsets import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'apartments', ApartmentViewSet)
router.register(r'apartment_media', ApartmentMediaViewSet)
router.register(r'apartment_amenities', ApartmentAmenitiesViewSet)
router.register(r'reservations', ReservationsViewSet)
router.register(r'cars', CarsViewSet)
router.register(r'car_media', CarMediaViewSet)
router.register(r'host', HostViewSet)
router.register(r'host_profile', HostProfileViewSet)
