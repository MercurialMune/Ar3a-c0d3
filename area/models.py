from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Area(models.Model):
    area_name = models.CharField(max_length=50, blank=True)
    area_photo = models.ImageField(upload_to='areapics/')
    population = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.area_name


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profpics/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)

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


class Business(models.Model):
    business_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField
    area = models.ForeignKey(Area, null=False, on_delete=models.CASCADE)

