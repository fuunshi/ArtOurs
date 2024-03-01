from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, UpdateView
from .models import ArtistProfile, Artwork
from .forms import ArtistProfileForm

class ArtistProfileDetailView(DetailView):
    model = ArtistProfile
    template_name = 'artists/artist_profile_detail.html'
    context_object_name = 'artist'

class ArtistProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ArtistProfile
    form_class = ArtistProfileForm
    template_name = 'artists/artist_profile_edit.html'
    success_url = reverse_lazy('artist-profile-detail')

    def get_success_url(self):
        return reverse('artists/artist-profile-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        # Additional processing if needed
        return response
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user == self.request.user:
            return obj
        else:
            return None

    def test_func(self):
        return self.get_object() is not None
