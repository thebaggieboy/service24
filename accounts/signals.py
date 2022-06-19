from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Profile

User = settings.AUTH_USER_MODEL
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(f'Profile created for account')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    print(f'Profile saved for account')