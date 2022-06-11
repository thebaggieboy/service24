from django.shortcuts import render
from django.views.generic import  TemplateView, CreateView, UpdateView, DeleteView, ListView 
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CarMediaSerializer, CarsSerializer, HostProfileSerializer, HostSerializer, UserSerializer, ApartmentSerializer, ReservationsSerializer, ApartmentMediaSerializer
from .models import Apartments, Host, Reservations, ApartmentMedia, Cars, CarMedia, HostProfile


class IndexView(TemplateView):
    template_name = "service24/index.html"

class RentalView(TemplateView):
    template_name = "service24/rentals.html"


class RegisterView(TemplateView):
    template_name = "service24/register.html"


class GetStartedView(TemplateView):
    template_name = "service24/get_started.html"


class BecomeAHostView(TemplateView):
    template_name = "service24/become_a_host.html"

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Apartments.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApartmentMediaViewset(viewsets.ModelViewSet):
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