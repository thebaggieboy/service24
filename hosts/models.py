from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.text import slugify 
from django.urls import reverse 

from .choices import BATHROOM_NO, BEDROOM_NO, CAR_TYPE, HOST_TYPE, NO_OF_GUESTS, TYPE
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Host(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email_address = models.CharField(max_length=250, null=True, blank=True)
    mobile_number = models.CharField(max_length=250, null=True, blank=True)
    host_name = models.CharField(max_length=250, null=True, blank=True)
    verified = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("apartments_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.host_name}')
        return super().save(*args, **kwargs)

    def __str__(self):
            return f'{self.host_name}'


class HostProfile(models.Model):
    host = models.OneToOneField(Host, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    display_picture = models.ImageField(upload_to='images/DP', null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True, default="Nigeria")
    state = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.CharField(max_length=250, null=True, blank=True)
    date_created = models.DateField(default=timezone.now())
    listed_apartments = models.ManyToManyField('Apartments')
    total_number_of_listed_apartments = models.IntegerField(null=True, blank=True)

    def get_total_no(self):
        total = HostProfile.objects.all.count()
        return total

    def get_absolute_url(self):
        return reverse("apartments_detail", kwargs={"slug": self.slug})


    def __str__(self):
            return f'Host Profile: {self.host}'

class Apartments(models.Model):
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
   
    images = models.ForeignKey('ApartmentMedia', on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("apartments_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class ApartmentAmenities(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, null=True, blank=True)
    no_of_bedrooms = models.CharField(max_length=250,null=True, blank=True, choices=BEDROOM_NO)
    no_of_bathrooms = models.CharField(max_length=250,null=True, blank=True, choices=BATHROOM_NO)
    no_of_guests = models.CharField(max_length=250,null=True, blank=True, choices=NO_OF_GUESTS)
    free_wifi = models.BooleanField(null=True, blank=True, default=False)
    air_condition = models.BooleanField(null=True, blank=True, default=False)
    heating = models.BooleanField(null=True, blank=True, default=False)
    washing_machine = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f'{self.apartment}'


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
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


    def __str__(self):
            return f'{self.apartment}'

class Cars(models.Model):

    name = models.CharField(max_length=250, null=True, blank=True)
    host = models.OneToOneField('Host', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    location = models.CharField(max_length=250)
    ratings = models.CharField(max_length=250)
    description = models.TextField()
    price = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(choices=CAR_TYPE, max_length=100, null=True, blank=True)
    listed_on = models.DateField(default=timezone.now())
    bluetooth = models.BooleanField(null=True, blank=True)
    air_condition = models.BooleanField(null=True, blank=True)
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
  

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.host}/{self.name}')
        return super().save(*args, **kwargs)
    def __str__(self):
        return f'Cars: {self.name}'

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
            return f'{self.car}'
