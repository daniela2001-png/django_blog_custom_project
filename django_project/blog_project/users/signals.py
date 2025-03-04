from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) -> None:
    """creates a profile after a user instance is saved
    
    Keyword arguments:
        sender -- The User model
        instance -- The  User instance associated
        created -- A boolean indicating whether the instance was just created
        kwargs -- optional parameter
    Return: None
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs) ->None:
    """Saves the Profile instance associated with the User instance
    Keyword arguments:
        sender -- The User model
        instance -- The  User instance associated
        kwargs -- optional parameter
    Return: None
    """
    instance.profile.save()