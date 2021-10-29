from django.shortcuts import redirect, render
from django.http import HttpResponse
from CV.models import CV, Position
from django.contrib import messages

from .forms import CvForm

# Create your views here.

def add_cv(request):
    if request.POST:
        form = CvForm(request.POST)
        
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone']
            url = form.cleaned_data['url']
            position = form.cleaned_data['position']
            technologies = form.cleaned_data['technologies']
            languages = form.cleaned_data['languages']
            motivation = form.cleaned_data['motivation']

            new_cv = CV(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                    url=url, position=position, technologies=technologies, languages=languages, motivation=motivation)
            new_cv.save()

            return redirect('/add-cv/')
        else:
            return render(request, 'add-cv.html', {"form": form})
    else:
        form = CvForm()

        return render(request, 'add-cv.html', {"form": form})


    # error = False

    # if request.POST:
    #     if 'first_name' in request.POST:
    #         first_name = request.POST.get('first_name', '')
    #         if not first_name:
    #             error = True
    #     else:
    #         error = True

    #     if 'last_name' in request.POST:
    #         last_name = request.POST.get('last_name', '')
    #         if not last_name:
    #             error = True
    #     else:
    #         error = True
        
    #     if 'email' in request.POST:
    #         email = request.POST.get('email', '')
    #         if not email:
    #             error = True
    #     else:
    #         error = True

    #     if 'phone_number' in request.POST:
    #         phone_number = request.POST.get('phone_number', '')
    #         if not phone_number:
    #             error = True
    #     else:
    #         error = True

    #     if 'url' in request.POST:
    #         url = request.POST.get('url', '')
    #     else:
    #         url = ""

    #     if 'position' in request.POST:
    #         position_id = request.POST.get('position', '')
    #         if not position_id:
    #             error = True
    #     else:
    #         error = True

    #     if 'technologies' in request.POST:
    #         technologies = request.POST.get('technologies', '')
    #         if not technologies:
    #             error = True
    #     else:
    #         error = True

    #     if 'languages' in request.POST:
    #         languages = request.POST.get('languages', '')
    #     else:
    #         languages = ""

    #     if 'motivation' in request.POST:
    #         motivation = request.POST.get('motivation', '')
    #         if not motivation:
    #             error = True
    #     else:
    #         error = True

    #     if not error:
    #         position = Position.objects.get(id = position_id)
    #         cv = CV(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
    #                 url=url, position=position, technologies=technologies, languages=languages, motivation=motivation)
    #         cv.save()

    #         messages.success(request, "You sent your CV.")
    #         return redirect('/add-cv/')
    #     else:
    #         messages.error(request, "Your CV is not send.")
    #         return redirect('/add-cv/')
    # else:
    #     positions = Position.objects.all()

    #     return render(request, 'add-cv.html', {"positions": positions})
            