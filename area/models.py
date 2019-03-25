from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Area(models.Model):
    area_name = models.CharField(max_length=50, blank=True)
    area_photo = models.ImageField(upload_to='areapics/')
    description = models.CharField(max_length=600, blank=True)
    resident = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profpics/')
    bio = models.CharField(max_length=600, blank=True)
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_user(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
