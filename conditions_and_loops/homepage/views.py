from django.shortcuts import render

# Create your views here.
def hello_page(request):
    property_1 = ("house")
    property_2 = ("apartament")
    property_3 = ("apartament")
    property_4 = ("house")
    properties = [property_1, property_2, property_3, property_4]

    return render(request, 'index.html', {"properties": properties})