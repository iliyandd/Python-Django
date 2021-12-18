from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import CreateUserForm, NoteForm

# Create your views here.

def user_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "You create new registration")

                return redirect('user_login')

        context = {"form": form}
        return render(request, 'register.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info("Incorrect username or password")

        return render(request, 'login.html')


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)

    return redirect('user_login')


@login_required(login_url='user_login')
def home(request):
    context = {"username": request.user.username}

    return render(request, 'home.html', context)


@login_required(login_url='user_login')
def about(request):
    context = {"to_home": '/', "username": request.user.username}

    return render(request, 'about.html', context)


@login_required(login_url='user_login')
def contacts(request):
    return render(request, 'contacts.html')

@login_required(login_url='user_login')
def display_notes(request):
    all_notes = Note.objects.filter(owner=request.user)

    notes = []
    for note in all_notes:
        item = {
            "title": note.title,
            "content": note.content,
            "owner": note.owner.username
        }
        notes.append(item)

    return JsonResponse({"notes": notes})
