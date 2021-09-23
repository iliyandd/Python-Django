from django.shortcuts import render
import time


def page(request):
    current_time = time.strftime("%H:%M:%S", time.localtime())

    return render(request, 'time.html', {"now": current_time})