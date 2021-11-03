from django import forms
from django.forms import ModelForm, fields
from .models import CV


class CVForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CVForm, self).__init__(*args, **kwargs)
        self.fields['url'].required = False

    class Meta:
        model = CV
        fields = '__all__' # or can I can list them in array
        widgets = {
            'first_name': forms.TextInput(attrs={
                'id': 'first_name',
                'class': 'less_text',
                'placeholder': "First name..."
            }),
            'last_name': forms.TextInput(attrs={
                'id': 'last_name',
                'class': 'less_text',
                'placeholder': "Last name..."
            }),
            'email': forms.TextInput(attrs={
                'id': 'email',
                'class': 'less_text',
                'placeholder': "Email..."
            }),
            'phone_number': forms.TextInput(attrs={
                'id': 'phone_number',
                'class': 'less_text',
                'placeholder': "Phone..."
            }),
            'url': forms.TextInput(attrs={
                'id': 'url',
                'class': 'less_text',
                'placeholder': "URL..."
            }),
            'position': forms.Select(attrs={
                'id': 'position',
                'class': 'choice'
            }),
            'technologies': forms.Textarea(attrs={
                'id': 'technologies',
                'class': 'text_area',
                'rows': '18',
                'cols': '80',
                'placeholder': 'Technologies...'
            }),
            'languages': forms.Textarea(attrs={
                'id': 'languages',
                'class': 'text_area',
                'rows': '7',
                'cols': '30',
                'placeholder': 'Languages...'
            }),
            'motivation': forms.Textarea(attrs={
                'id': 'motivation',
                'class': 'text_area',
                'rows': '10',
                'cols': '80',
                'placeholder': 'Motivation...'
            })
        }


# class CvForm(forms.Form):
#     first_name = forms.CharField(label="First name", max_length=30, required=True, widget=forms.TextInput(attrs={
#         "style": "\
#             width: 200px;\
#             height: 20px;\
#             border: 2px solid grey;\
#             font-size: 17px;\
#             padding: 4px;\
#             font-family: Arial;",
#         "placeholder": "First name"
#     }))
#     last_name = forms.CharField(label="Last name", max_length=30, required=True, widget=forms.TextInput)
#     email = forms.EmailField(label="Email", required=True)
#     phone = forms.CharField(label="Phone", max_length=50, required=True)
#     url = forms.CharField(label="URL", max_length=150, required=False, widget=forms.TextInput)
#     position = forms.ModelChoiceField(label="Position", queryset=Position.objects.all())
#     technologies = forms.CharField(label="Technologies", widget=forms.Textarea)
#     languages = forms.CharField(label="Languages", widget=forms.TextInput)
#     motivation = forms.CharField(label="Motivation", widget=forms.Textarea)
