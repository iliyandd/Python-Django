from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required # If user is not loged in, he can't visit some of pages

from .forms import CVForm, CreateUserForm
from .models import CV

# Create your views here.

@login_required(login_url='login') # restricted
def add_cv(request):
    form = CVForm()

    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('add_cv')
    else:
        return render(request, 'add-cv.html', {"form": form})


def user_register(request):
    # If user isn't authenticated, he can't make new registration.
    if request.user.is_authenticated:
        return redirect('add_cv')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "You create new registration.")

                return redirect('login')

        context = {"form": form}

        return render(request, 'register.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('add_cv')
        else:
            messages.info(request, "Username or password is incorrect.")

    return render(request, 'login.html')


@login_required(login_url='login') # restricted
def user_logout(request):
    logout(request)

    return redirect('login')


# def add_cv(request):
#     if request.POST:
#         form = CvForm(request.POST)
        
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             phone_number = form.cleaned_data['phone']
#             url = form.cleaned_data['url']
#             position = form.cleaned_data['position']
#             technologies = form.cleaned_data['technologies']
#             languages = form.cleaned_data['languages']
#             motivation = form.cleaned_data['motivation']

#             new_cv = CV(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
#                     url=url, position=position, technologies=technologies, languages=languages, motivation=motivation)
#             new_cv.save()

#             return redirect('/add-cv/')
#         else:
#             return render(request, 'add-cv.html', {"form": form})
#     else:
#         form = CvForm()

#         return render(request, 'add-cv.html', {"form": form})
