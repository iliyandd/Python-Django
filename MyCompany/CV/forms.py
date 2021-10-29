from django import forms
from django.forms import fields, widgets
from CV.models import Position


class CvForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=30, required=True, widget=forms.TextInput(attrs={
        "style": "\
            width: 200px;\
            height: 20px;\
            border: 2px solid grey;\
            font-size: 17px;\
            padding: 4px;\
            font-family: Arial;",
        "placeholder": "First name"
    }))
    last_name = forms.CharField(label="Last name", max_length=30, required=True, widget=forms.TextInput)
    email = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(label="Phone", max_length=50, required=True)
    url = forms.CharField(label="URL", max_length=150, widget=forms.TextInput)
    position = forms.ModelChoiceField(label="Position", queryset=Position.objects.all())
    technologies = forms.CharField(label="Technologies", widget=forms.Textarea)
    languages = forms.CharField(label="Languages", widget=forms.TextInput)
    motivation = forms.CharField(label="Motivation", widget=forms.Textarea)
