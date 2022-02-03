from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import NoteForm


@login_required(login_url='/login/')
def home(request):
    context = {"username": request.user.username}

    return render(request, 'home.html', context)


@login_required(login_url='/login/')
def about(request):
    context = {"to_home": '/', "username": request.user.username}

    return render(request, 'about.html', context)


@login_required(login_url='/login/')
def contacts(request):
    context = {"to_home": '/', "username": request.user.username}

    return render(request, 'contacts.html', context)


@login_required(login_url='/login/')
def display_notes(request):
    all_notes = Note.objects.filter(owner=request.user)

    notes = []
    for note in all_notes:
        item = {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "owner": note.owner.username,
            "created": note.created,
            "updated": note.updated
        }
        notes.append(item)

    return JsonResponse({"notes": notes})


@login_required(login_url='/login/')
def new_note(request):
    form = NoteForm()

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        try:
            Note(title=title, content=content, owner=request.user).save()
        except Exception:
            messages.error(request, "Unsuccessfuly adding of new note.")
        else:
            messages.success(request, "You added new note.")

        return redirect('/')

    context = {"to_home": '/', "username": request.user.username, "form": form}

    return render(request, 'new_note.html', context)


@login_required(login_url='/login/')
def delete_note(request):
    if request.method == "POST":
        note_id = request.POST.get("note_id")
        
        Note.objects.get(id=note_id).delete()

        return HttpResponse('')


@login_required(login_url='/login/')
def edit_note(request):
    if request.method == "POST":
        note_id = request.POST.get("note_id")
        title = request.POST.get("title")
        content = request.POST.get("content")

        Note.objects.filter(id=note_id).update(title=title, content=content)

        return HttpResponse('')
