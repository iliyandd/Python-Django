from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'username',
                'class': 'registration_input',
                'autocomplete': 'off',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'class': 'registration_input',
                'autocomplete': 'off',
            }),
            'password1': forms.PasswordInput(attrs={
                'id': 'id_password1',
                'class': 'registration_input',
                'autocomplete': 'off',
            }),
            'password2': forms.PasswordInput(attrs={
                'id': 'id_password2',
                'class': 'registration_input',
                'autocomplete': 'off',
            }),
        }