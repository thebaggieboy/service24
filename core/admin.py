from django.contrib import admin
from django.contrib import messages  
# Register your models here.
from .models import Apartments, ApartmentMedia, Reservations, Cars, CarMedia, HostProfile, Host


@admin.register(Apartments)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('host', 'name', 'location', 'ratings', 'map', 'description', 'price_per_night', 'type', 'listed_on')

admin.site.register(ApartmentMedia)
admin.site.register(CarMedia)
admin.site.register(Host)
admin.site.register(HostProfile)
   
@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):
    list_display = ('host', 'name', 'location', 'ratings', 'description', 'price', 'type', 'listed_on')


admin.site.register(Reservations)