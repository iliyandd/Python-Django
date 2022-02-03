from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm


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

                return redirect('/login/')

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


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)

    return redirect('/login/')