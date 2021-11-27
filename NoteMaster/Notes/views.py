from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import CreateUserForm, NoteForm

# Create your views here.

def user_register(request):
    if request.user.is_authenticated:
        user_id = request.user.id

        return redirect(f'home/{user_id}/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success("You create new registration")

                return redirect('user_login')

        context = {"form": form}
        return render(request, 'register.html', context)                



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user_id = str(user.id)

            return redirect(f'home/{user_id}/')
        else:
            messages.info("Username or password is incorrect")

    return render(request, 'login.html')


# @login_required(login_url='user_login')
def home(request, uid):
    all_notes = Note.objects.filter(owner=uid)

    return render(request, 'home.html', {"all_notes": all_notes})


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')