from django import forms
from django.forms import ModelForm
from .models import Note


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
                'autocomplete': 'off',
                'placeholder': 'Title...',
            }),
            'content': forms.Textarea(attrs={
                'id': 'note-content',
                'rows': '10',
                'cols': '40',
                'placeholder': 'Content...',
            }) 
        }