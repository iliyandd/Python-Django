from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Note

# Create your views here.

# @login_required(login_url='login')
def home(request):
    all_notes = Note.objects.all()

    return render(request, 'home.html', {"all_notes": all_notes})


def about(request):
    pass


def contacts(request):
    pass