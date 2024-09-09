from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

# Create your views here.

def inscription(request):
    if request.method == 'POST':
        form = Inscription_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('liste')
        
    else:
        form = Inscription_Form()
    
    return render(request, 'inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
            
    else:

        form = AuthenticationForm()
    
    return render(request, 'connexion.html', {'form':form})


def deconnexion(request):
    logout(request)
    return redirect('accueil')