from django.shortcuts import render
from django.views.generic import  TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from accounts.models import User, Profile
from core.models import Reservations
from hosts.models import *
from .serializers import ApartmentAmenitiesSerializer, ProfileSerializer, UserSerializer, ApartmentMediaSerializer, ApartmentSerializer, HostProfileSerializer, HostSerializer, CarMediaSerializer, CarsSerializer, ReservationsSerializer
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-date_created')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]



class ApartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Apartments.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApartmentAmenitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ApartmentAmenities.objects.all()
    serializer_class = ApartmentAmenitiesSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApartmentMediaViewSet(viewsets.ModelViewSet):
    queryset = ApartmentMedia.objects.all()
    serializer_class = ApartmentMediaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarMediaViewSet(viewsets.ModelViewSet):
    queryset = CarMedia.objects.all()
    serializer_class = CarMediaSerializer
    permission_classes = [permissions.IsAuthenticated]

class HostProfileViewSet(viewsets.ModelViewSet):
    queryset = HostProfile.objects.all()
    serializer_class = HostProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    permission_classes = [permissions.IsAuthenticated]
