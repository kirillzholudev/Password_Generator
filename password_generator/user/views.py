from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistrationForm


def home(request):
    return render(request, 'user/home.html')


def register(request):
    user = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('generate_password')
    else:
        form = RegistrationForm()

    return render(request, 'user/registration.html', {'form': form, 'user': user})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('generate_password')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})