from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_artist = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='user_profile', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)

class Artist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='artist_user')
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='artist_profile', blank=True, null=True)
    available_for_commission = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Customer(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='customer_user')
    

    def __str__(self):
        return self.user.username
    
