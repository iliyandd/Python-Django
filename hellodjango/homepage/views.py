from django.shortcuts import render


def page(request):
    first_name = "Iliyan"
    last_name = "Dimitrov"
    age = 20
    parents = ["Dimitar", "Aneta"]

    return render(request, 'index.html', {"first": first_name, "last": last_name, "age": age, "parents": parents})