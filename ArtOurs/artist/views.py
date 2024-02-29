from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Artist, Artwork

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def profile(request):
    user = request.user
    if user.is_artist:
        artist = Artist.objects.get(user=user)
        artwork = Artwork.objects.filter(artist=artist)
        return render(request, 'artist_profile.html', {'artist': artist, 'artwork': artwork})
    else:
        return render(request, 'buyer_profile.html', {'user': user})
