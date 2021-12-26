from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Note


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'username',
                'class': 'registration_input',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'class': 'registration_input',
            }),
            'password1': forms.PasswordInput(attrs={
                'id': 'id_password1',
                'class': 'registration_input',
            }),
            'password2': forms.PasswordInput(attrs={
                'id': 'id_password2',
                'class': 'registration_input',
            }),

        }

class NoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False

    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'note-title',
                'placeholder': 'Title',
                'autocomplete': 'off'
            }),
            'content': forms.Textarea(attrs={
                'id': 'note-content',
                'rows': '10',
                'cols': '40'
            }) 
        }