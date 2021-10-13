from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'test.html')

def add_cv(request):
    pass