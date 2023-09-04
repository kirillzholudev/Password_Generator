import random
import string

from django.shortcuts import render, redirect, get_object_or_404

from .forms import PasswordSettingsForm, SavedPasswordForm
from .models import PasswordSettings, SavedPassword


def generate_password(request):
    user = request.user
    password_settings, created = PasswordSettings.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = PasswordSettingsForm(request.POST, instance=password_settings)
        if form.is_valid():
            form.save()
            generated_password = generate_custom_password(password_settings)
            request.session['generated_password'] = generated_password
            request.session.modified = True
            return redirect('save_password')
    else:
        form = PasswordSettingsForm(instance=password_settings)

    return render(request, 'generator/password.html', {'form': form})


def generate_custom_password(password_settings):
    characters = string.ascii_lowercase
    characters += string.ascii_uppercase if password_settings.use_uppercase else ""
    characters += string.digits if password_settings.use_numbers else ""
    characters += string.punctuation if password_settings.use_special_characters else ""

    password = ''.join(random.choice(characters) for _ in range(password_settings.password_length))

    return password


def saved_passwords(request):
    saved_passwords = SavedPassword.objects.filter(user=request.user)

    return render(request, 'generator/saved_passwords.html', {'saved_passwords': saved_passwords})


def save_password(request):
    generated_password = request.session.get('generated_password')  # Извлекаем сгенерированный пароль из сессии

    if request.method == 'POST':
        form = SavedPasswordForm(request.POST)

        if form.is_valid():
            saved_password = form.save(commit=False)
            saved_password.user = request.user
            saved_password.password = generated_password  # Сохраняем сгенерированный пароль
            saved_password.save()
            return redirect('generate_password')

    else:
        form = SavedPasswordForm(initial={'generated_password': generated_password})

    return render(request, 'generator/save_password.html', {'form': form, 'generated_password': generated_password})


def delete_password(request, password_id):
    password = get_object_or_404(SavedPassword, id=password_id)
    if request.method == 'POST':
        password.delete()
        return redirect('saved_passwords')
    return render(request, 'generator/delete_password_confirmation.html', {'password': password})