from django.urls import path
from .views import *

urlpatterns = [
    path('art/<int:pk>/', ArtistProfileDetailView.as_view(), name='artist-profile-detail'),
    path('art/<int:pk>/edit/', ArtistProfileUpdateView.as_view(), name='artist-profile-edit'),
]
