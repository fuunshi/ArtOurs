from django.db import models
from custom_auth.models import CustomUser

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True)
    wishlist = models.ManyToManyField('Artwork', related_name='wishlisted_customers', blank=True)

    def __str__(self):
        return self.user.username
