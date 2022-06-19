from django import forms 
from .models import Host, HostProfile, Apartments, ApartmentAmenities

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['first_name', 'last_name', 'email_address', 'mobile_number', 'host_name']



"""class HostForm(forms.ModelForm):
    class Meta:
        model = HostProfile
       

class HostForm(forms.ModelForm):
    class Meta:
        model = Apartments
       

class HostForm(forms.ModelForm):
    class Meta:
        model = ApartmentAmenities
"""

