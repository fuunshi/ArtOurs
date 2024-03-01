from django.db import models
from custom_auth.models import CustomUser

class ArtistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True)
    portfolio_link = models.URLField(blank=True)
    is_available_for_commission = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Artwork(models.Model):
    artist_name = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE, related_name='artworks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title