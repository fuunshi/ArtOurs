from django.shortcuts import render, redirect
from django.contrib.auth import login
from .managers import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'custom_auth/signup.html', {'form': form})

def login(request):
    return render(request, 'custom_auth/login.html', {})

def logout(request):
    pass