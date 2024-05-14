from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ArtistForm, ArtistRegistrationForm
from .models import Artist
from marketplace.models import Artwork

def index(request):
    hot_artworks = Artwork.objects.order_by('-likes')[:4]
    return render(request, 'core/index.html', {'hot_artworks':hot_artworks})

def search(request):
    query = request.GET.get('q')
    if query:
        artwork_results = Artwork.objects.filter(title__icontains=query)
        artist_results = Artist.objects.filter(user__username__icontains=query)
    else:
        artwork_results = artist_results = None
    return render(request, 'core/search/search_result.html', {
        'artwork_results': artwork_results,
        'artist_results': artist_results, 
        'query': query
        })

def editprofile(request):
    user = request.user
    return render(request, 'core/editartistprofile.html')

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def register_as_artist(request):
    if request.method == 'POST':
        form = ArtistRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.user = request.user
            artist.save()
            request.user.is_artist = True
            request.user.save()
            return redirect('index')  # Redirect to the artist profile page
    else:
        form = ArtistRegistrationForm()
    return render(request, 'core/register_artist.html', {'form': form})

def get_artist_by_name(name):
    User = get_user_model()
    custom_user = get_object_or_404(User, username=name)
    artist = get_object_or_404(Artist, user=custom_user)
    return artist

def artist_profile(request, artist_username):
    artist = get_artist_by_name(artist_username)
    return render(request, 'core/profile/artist_profile.html', { 'artist':artist })

@login_required
def edit_profile(request, artist_username):
    artist = get_object_or_404(Artist, user__username=artist_username)
    
    # Check if the logged-in user is the owner of the profile
    if request.user != artist.user:
        return HttpResponseForbidden("You don't have permission to edit this profile.")
    
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_profile', artist_username=artist_username)
    else:
        form = ArtistForm(instance=artist)
    
    return render(request, 'core/profile/edit_profile.html', {'form': form})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'core/profile/artist_list.html', {'artists': artists})