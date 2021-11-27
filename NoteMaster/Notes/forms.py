from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import Note, MyUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']


class NoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False

    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'note_title',
                'placeholder': 'Title'
            }),
            'content': forms.Textarea(attrs={
                'id': 'note_content',
                'rows': '10',
                'cols': '40'
            }) 
        }