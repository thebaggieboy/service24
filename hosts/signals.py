from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import  Host, Apartments, ApartmentMedia, HostProfile, ApartmentAmenities

@receiver(post_save, sender=Host)
def create_host_profile(sender, instance, created, **kwargs):
    if created:
        HostProfile.objects.create(host=instance)
        print(f'[SIGNAL] - Profile created for host')



@receiver(post_save, sender=Apartments)
def create_apartment_profile(sender, instance, created, **kwargs):
    if created:
        ApartmentMedia.objects.create(apartment=instance)
        ApartmentAmenities.objects.create(apartment=instance)
        print(f'[SIGNAL] - Media and amenities model created for apartment')

