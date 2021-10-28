from django.shortcuts import render, redirect
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required

from email_messages.forms import MessageForm

# Create your views here.

@login_required
def message_to_user(request):
    if request.method == "POST":
        form = MessageForm(request, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('/message_to_user_done/')
    else:
        form = MessageForm(request)

    return render(request, "message_to_user.html", {"form": form})