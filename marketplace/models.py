from django.db import models
from core.models import CustomUser, Artist

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='artworks')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    likes = models.ManyToManyField(CustomUser, related_name='liked_artworks', blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    STARS_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )

    content = models.TextField()
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS_CHOICES)  # Field for star rating

    def __str__(self):
        return f"Review for {self.artwork.title} by {self.user.username}"