from django.urls import path, include
from .views import (
    index,
    search,
    # profile,
    editprofile,
    SignupView,
    register_as_artist,

    artist_list,
    artist_profile,
    edit_profile,
)

urlpatterns = [
    path("", index, name='index'),
    path("search/", search, name='search'),
    path("accounts/register/", SignupView.as_view(), name='register'),
    path("accounts/register/artist", register_as_artist, name='register_artist'),
    path("accounts/editprofile/", editprofile, name='editprofile'),
    # path("accounts/profile/", profile, name='profile'),
    path("accounts/", include('django.contrib.auth.urls')),

    # Urls for Profile Mangement
    path("artist/", artist_list, name='artist_list'),
    path("artist/<str:artist_username>/", artist_profile, name='artist_profile'),
    path("artist/<str:artist_username>/edit", edit_profile, name='edit_profile'),
]
