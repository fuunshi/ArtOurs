from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_artist = models.BooleanField(default=False)

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='artist_profile')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    medium = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='artwork_images')
    categories = models.ManyToManyField('Category')

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
