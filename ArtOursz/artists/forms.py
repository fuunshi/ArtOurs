from django import forms
from .models import ArtistProfile

class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = ArtistProfile
        fields = ['bio', 'portfolio_link', 'is_available_for_commission']
