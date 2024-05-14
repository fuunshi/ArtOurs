from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

from .models import Artwork, Review
from .forms import ArtworkForm, ReviewForm
from core.models import Artist

def marketplace(request):
    artworks = Artwork.objects.all()
    context = {'artworks': artworks}
    return render(request, 'marketplace/marketlist.html', context)

def artwork_detail(request, artwork_id):
    artwork = Artwork.objects.get(pk=artwork_id)
    context = {
        'artwork': artwork,
    }
    return render(request, 'marketplace/marketdetail.html', context)

@login_required
def add_artwork(request):
    # Check if the user is authenticated and is an artist
    if not (request.user.is_authenticated and request.user.is_artist):
        return redirect('login') 

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        # Get the artist associated with the logged-in user
        User = get_user_model()
        custom_user = get_object_or_404(User, username=request.user.username)
        artist = get_object_or_404(Artist, user=custom_user)


        # Create a new Artwork instance
        artwork = Artwork.objects.create(
            title=title,
            description=description,
            price=price,
            image=image,
            artist=artist
        )

        return redirect('marketplace')

    return render(request, 'marketplace/add_artwork.html')

@login_required
def like_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    user = request.user
    if artwork.likes.filter(pk=user.pk).exists():
        artwork.likes.remove(user)
    else:
        artwork.likes.add(user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('marketplace')))

@login_required
def add_review(request, artwork_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.artwork_id = artwork_id
            review.user = request.user  # Assuming the user is authenticated
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('artwork_detail', artwork_id=artwork_id)
        else:
            messages.error(request, 'Error adding review. Please check your input.')
    else:
        form = ReviewForm()
    return render(request, 'marketplace/review_views/add_review.html', {'form': form})
    
@login_required
def edit_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artwork_detail', artwork_id=artwork.id)  # Redirect to the artwork detail page
    else:
        form = ArtworkForm(instance=artwork)
    return render(request, 'marketplace/edit_artwork.html', {'form': form, 'artwork': artwork})


@login_required
def delete_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    if request.user.is_authenticated and request.user.username == artwork.artist.user.username:
        artwork.delete()
        return redirect('marketplace') 
    else:
        return redirect('home') # TODOPermission Denied URL