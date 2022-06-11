from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.text import slugify  

from .choices import BATHROOM_NO, BEDROOM_NO, CAR_TYPE, HOST_TYPE, NO_OF_GUESTS, TYPE
from django.contrib.auth import get_user_model

User = get_user_model()

class Apartments(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    host = models.OneToOneField('Host', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    ratings = models.CharField(max_length=250, null=True, blank=True)
    map = models.CharField(max_length=250)
    description = models.TextField()
    price_per_night = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(choices=TYPE, max_length=100, null=True, blank=True)
    listed_on = models.DateField(default=timezone.now())
    no_of_bedrooms = models.CharField(max_length=250,null=True, blank=True, choices=BEDROOM_NO)
    no_of_bathrooms = models.CharField(max_length=250,null=True, blank=True, choices=BATHROOM_NO)
    no_of_guests = models.CharField(max_length=250,null=True, blank=True, choices=NO_OF_GUESTS)
    wifi = models.BooleanField(null=True, blank=True)
    air_condition = models.BooleanField(null=True, blank=True)
    images = models.ForeignKey('ApartmentMedia', on_delete=models.CASCADE, null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ApartmentMedia(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, null=True, blank=True)
    display_image = models.ImageField(null=True, blank=True, upload_to='media')
    interior_image_1 = models.ImageField(null=True, blank=True)
    interior_image_2 = models.ImageField(null=True, blank=True)
    interior_image_3 = models.ImageField(null=True, blank=True)
    interior_image_4 = models.ImageField(null=True, blank=True)
    interior_image_5 = models.ImageField(null=True, blank=True)
    exterior_image_1 = models.ImageField(null=True, blank=True)
    exterior_image_2 = models.ImageField(null=True, blank=True)
    exterior_image_3 = models.ImageField(null=True, blank=True)
    exterior_image_4 = models.ImageField(null=True, blank=True)
    exterior_image_5 = models.ImageField(null=True, blank=True)
    

    def __str__(self):
            return self.apartment

class Reservations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, null=True, blank=True)
    booked = models.BooleanField(default=False)
    booking_date = models.DateField(default=timezone.now())
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
 

    def __str__(self):
        return self.apartment


class Cars(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    host = models.OneToOneField('Host', on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=250)
    ratings = models.CharField(max_length=250)
    description = models.TextField()
    price = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(choices=CAR_TYPE, max_length=100, null=True, blank=True)
    listed_on = models.DateField(default=timezone.now())
    bluetooth = models.BooleanField(null=True, blank=True)
    air_condition = models.BooleanField(null=True, blank=True)
    

    def __str__(self):
        return self.name

class CarMedia(models.Model):
    car = models.OneToOneField(Cars, on_delete=models.CASCADE, null=True, blank=True)
    display_image = models.ImageField(null=True, blank=True, upload_to='media')
    interior_image_1 = models.ImageField(null=True, blank=True)
    interior_image_2 = models.ImageField(null=True, blank=True)
    interior_image_3 = models.ImageField(null=True, blank=True)
    interior_image_4 = models.ImageField(null=True, blank=True)
    interior_image_5 = models.ImageField(null=True, blank=True)
    exterior_image_1 = models.ImageField(null=True, blank=True)
    exterior_image_2 = models.ImageField(null=True, blank=True)
    exterior_image_3 = models.ImageField(null=True, blank=True)
    exterior_image_4 = models.ImageField(null=True, blank=True)
    exterior_image_5 = models.ImageField(null=True, blank=True)
    

    def __str__(self):
            return self.car



class Host(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    service_type = models.CharField(max_length=250, null=True, blank=True, choices=HOST_TYPE)
    business_name =models.CharField(max_length=250, null=True, blank=True)
    verified = models.BooleanField(default=False)


    def __str__(self):
            return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile_number = models.CharField(max_length=250, null=True, blank=True)
    email_address = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.CharField(max_length=250, null=True, blank=True)
    number_of_bookings = models.CharField(max_length=250, null=True, blank=True)
    date_created = models.DateField(default=timezone.now())
    

class HostProfile(models.Model):
    host = models.OneToOneField(Host, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='images', null=True, blank=True)
    mobile_number = models.CharField(max_length=250, null=True, blank=True)
    email_address = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True, default="Nigeria")
    city = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.CharField(max_length=250, null=True, blank=True)
    
    date_created = models.DateField(default=timezone.now())
    listed_apartments = models.ManyToManyField(Apartments)
    no_of_apartments = models.IntegerField(null=True, blank=True)



    def __str__(self):
            return self.host


