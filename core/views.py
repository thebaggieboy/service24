from django.shortcuts import render
from django.views.generic import  TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.models import User, Group

#from .serializers import CarMediaSerializer, CarsSerializer, HostProfileSerializer, HostSerializer, UserSerializer, ApartmentSerializer, ReservationsSerializer, ApartmentMediaSerializer
from .models import Apartments


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



class ApartmentDetailView(DetailView):
    model = Apartments

class ApartmentCreateView(CreateView):
    model = Apartments
    template_name = 'service24/list_apartment.html'

