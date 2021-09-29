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

    # This will load only projects associated with me.
    # all_projects = Project.objects.filter(client_name="Iliyan")

    # Displays the first project which satisfies the criteria.
    # all_projects = Project.objects.get(client_name="Iliyan")

    return render(request, 'displaying.html', {"action": "Display all projects.", "all_projects": all_projects})