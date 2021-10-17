from django.shortcuts import render
from django.http import HttpResponse
from CV.models import CV, Position

# Create your views here.

def test(request):
    return render(request, 'test.html')

def add_cv(request):
    error = False

    if request.POST:
        if 'first_name' in request.POST:
            first_name = request.POST.get('first_name', '')
        else:
            error = True

        if 'last_name' in request.POST:
            last_name = request.POST.get('last_name', '')
        else:
            error = True
        
        if 'email' in request.POST:
            email = request.POST.get('email', '')
        else:
            error = True

        if 'phone_number' in request.POST:
            phone_number = request.POST.get('phone_number', '')
        else:
            error = True

        if 'url' in request.POST:
            url = request.POST.get('url', '')
        else:
            url = ""

        if 'position' in request.POST:
            position_id = request.POST.get('position', '')
        else:
            error = True

        if 'technologies' in request.POST:
            technologies = request.POST.get('technologies', '')
        else:
            error = True

        if 'languages' in request.POST:
            languages = request.POST.get('languages', '')
        else:
            languages = ""

        if 'motivation' in request.POST:
            motivation = request.POST.get('motivation', '')
        else:
            error = True

        if not error:
            position = Position.objects.get(id = position_id)
            cv = CV(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                    url=url, position=position, technologies=technologies, languages=languages, motivation=motivation)
            cv.save()

            return HttpResponse("Your CV is added.")
        else:
            return HttpResponse("An error is occured.")
    else:
        positions = Position.objects.all()

        return render(request, 'add-cv.html', {"positions": positions})


            