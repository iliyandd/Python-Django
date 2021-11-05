from django.shortcuts import redirect, render

from .forms import CVForm

# Create your views here.

def add_cv(request):
    form = CVForm()

    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/add-cv/')
    else:
        return render(request, 'add-cv.html', {"form": form})


def register(request):
    pass


def login(request):
    pass


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
