from django.contrib.auth.models import User
from rest_framework import serializers
#from .models import Apartments, Reservations, ApartmentMedia, Cars, CarMedia, HostProfile, Host
from accounts.models import User, Profile
from core.models import Reservations
from hosts.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'email']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'display_picture', 'date_created']



class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apartments
        fields = ['name', 'host', 'location', 'ratings', 'map', 'description', 'price_per_night', 'type', 'no_of_bedrooms', 'no_of_bathrooms']


class ApartmentAmenitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApartmentAmenities
        fields = ['apartment', 'no_of_bedrooms', 'no_of_bathrooms', 'free_wifi', 'air_condition', 'heating', 'washing_machine']


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
        fields = ['host', 'display_picture', 'bio', 'date_created', 'country', 'state', 'city', 'address', 'zip_code', 'listed_apartments', 'total_number_of_listed_apartments']
        
class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ['first_name', 'last_name' , 'email_address', 'mobile_number', 'host_name','verified']
