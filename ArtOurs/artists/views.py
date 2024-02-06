from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from .models import ArtistProfile, Artwork
from .forms import ArtistProfileForm

class ArtistProfileDetailView(DetailView):
    model = ArtistProfile
    template_name = 'artists/artist_profile_detail.html'
    context_object_name = 'artist'

class ArtistProfileUpdateView(UpdateView):
    model = ArtistProfile
    form_class = ArtistProfileForm
    template_name = 'artists/artist_profile_edit.html'

    def get_success_url(self):
        return reverse('artists/artist-profile-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        # Additional processing if needed
        return response
