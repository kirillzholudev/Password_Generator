from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        # Устанавливаем классы CSS для полей и меток (label)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'registration-input'
            self.fields[field_name].label = ''
