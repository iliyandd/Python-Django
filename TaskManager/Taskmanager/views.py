from django.shortcuts import render
from Taskmanager.models import Project

# Create your views here.

def save_project(request):
    new_project = Project(title="Google", description="Web browser", client_name="Iliyan")
    new_project.save()

    return render(request, 'saving.html', {'action': 'Save datas of model.'})


def hello(request):
    return render(request, 'index.html')


def display_projects(request):
    all_projects = Project.objects.all()
    return render(request, 'displaying.html', {"action": "Display all projects.", "all_projects": all_projects})