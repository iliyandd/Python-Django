from django.shortcuts import render
from django.db.models import Q
from Taskmanager.models import Project, Task

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

    # Updates description of existing task.(Method 1)
    # task = Task.objects.get(title="Task 1")
    # task.description = "New description"
    # task.save()

    # Updates description of existing task.(Method 2)
    # Task.objects.filter(title="Task 1").update(title="New task 1")

    # Deletes one/multiple record/s.
    # one_task = Task.objects.get(id = 1)
    # one_task.delete()

    # Using OR operator.
    # project_list = Project.objects.filter(Q(client_name="Iliyan") | Q(client_name="Spasimira"))

    # Lower and greater than lookups
    # frequent_tasks = Task.objects.filter(time_elapsed__gte = 4)

    # Making a raw SQL query.
    # all_projects = Project.objects.raw("SELECT * FROM TaskManager_project")


    return render(request, 'displaying.html', {"action": "Display all projects.", "all_projects": all_projects})