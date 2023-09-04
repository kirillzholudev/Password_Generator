from django import forms
from .models import PasswordSettings, SavedPassword


class PasswordSettingsForm(forms.ModelForm):
    class Meta:
        model = PasswordSettings
        fields = ['use_special_characters', 'use_uppercase', 'use_numbers', 'password_length']


class SavedPasswordForm(forms.ModelForm):
    generated_password = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = SavedPassword
        fields = ['password', 'description']

    password = forms.CharField(widget=forms.HiddenInput(), required=False)