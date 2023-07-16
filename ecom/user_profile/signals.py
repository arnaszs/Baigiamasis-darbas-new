from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def sync_profile(sender, instance, created, **kwargs) -> None:
    if created:
        Profile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()
        else:
            Profile.objects.create(user=instance)
