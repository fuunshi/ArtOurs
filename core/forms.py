from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Artist
from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', max_length=255, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', max_length=255, required=True, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self) -> str:
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['bio', 'website', 'profile_picture', 'available_for_commission']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'website': forms.URLInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'profile_picture': forms.FileInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'available_for_commission': forms.CheckboxInput(attrs={'class': 'form-checkbox rounded text-blue-500'}),
        }

class ArtistRegistrationForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['bio', 'website', 'profile_picture', 'available_for_commission']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'block w-full px-4 py-2 leading-tight rounded-lg shadow-md bg-gray-100 text-gray-800 focus:outline-none focus:bg-white focus:border-blue-500'}),
            'website': forms.URLInput(attrs={'class': 'block w-full px-4 py-2 leading-tight rounded-lg shadow-md bg-gray-100 text-gray-800 focus:outline-none focus:bg-white focus:border-blue-500'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'block w-full px-4 py-2 leading-tight rounded-lg shadow-md bg-gray-100 text-gray-800 focus:outline-none focus:bg-white focus:border-blue-500'}),
            'available_for_commission': forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 text-blue-600'}),
        }