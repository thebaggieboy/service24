from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.text import slugify 
from django.urls import reverse 
from .choices import BATHROOM_NO, BEDROOM_NO, CAR_TYPE, HOST_TYPE, NO_OF_GUESTS, TYPE
from django.contrib.auth import get_user_model
from hosts.models import Apartments
User = get_user_model()



class Reservations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, null=True, blank=True)
    booked = models.BooleanField(default=False)
    booking_date = models.DateField(default=timezone.now())
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)

    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


    def __str__(self):
        return f'{self.apartment}'

