from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Apartments, Reservations, ApartmentMedia, Cars, CarMedia, HostProfile, Host

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apartments
        fields = ['name', 'host', 'location', 'ratings', 'map', 'description', 'price_per_night', 'type', 'no_of_bedrooms', 'no_of_bathrooms']

class ReservationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservations
        fields = ['apartment', 'booked', 'booking_date', 'check_in_date', 'check_out_date']

class ApartmentMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApartmentMedia
        fields = ['display_image', 'interior_image_1', 'interior_image_2', 'interior_image_3', 'interior_image_4', 'interior_image_5', 'exterior_image_1', 'exterior_image_2', 'exterior_image_3', 'exterior_image_4', 'exterior_image_5', ]

class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ['name', 'location', 'ratings', 'description', 'price', 'type', 'listed_on', 'bluetooth', 'air_condition' ]

class CarMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarMedia
        fields = ['car', 'display_image', 'interior_image_1', 'interior_image_2', 'interior_image_3', 'interior_image_4', 'interior_image_5', 'exterior_image_1', 'exterior_image_2', 'exterior_image_3', 'exterior_image_4', 'exterior_image_5']

class HostProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostProfile
        fields = ['host', 'logo', 'bio', 'date_created', 'mobile_number', 'email_address', 'state', 'city', 'address', 'zip_code']
        
class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'service_type', 'business_name', 'verified']
