from django.contrib import admin
from django.contrib import messages  
# Register your models here.
from .models import Reservations


admin.site.register(Reservations)