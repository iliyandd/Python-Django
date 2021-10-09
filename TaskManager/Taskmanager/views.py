from django.shortcuts import render
from Taskmanager.models import Project, Developer, Supervisor
from django.http import HttpResponse
from django import forms

# Create your views here.

def hello(request):
    return render(request, 'index.html')


def save_project(request):
    new_project = Project(title="Google", description="Web browser", client_name="Iliyan")
    new_project.save()

    return render(request, 'saving.html', {'action': 'Save datas of model.'})


def display_projects(request):
    all_supervisors = Supervisor.objects.all()

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


    return render(request, 'displaying.html', {"action": "Display all supervisors.", "all_supervisors": all_supervisors})


# using HTML form
# def create_developer(request):
#     error = False

#     # If form has posted
#     if request.POST:
#         if 'name' in request.POST:
#             name = request.POST.get('name', '')
#         else:
#             error = True

#         if 'login' in request.POST:
#             login = request.POST.get('login', '')
#         else:
#             error = True

#         if 'password' in request.POST:
#             password = request.POST.get('password', '')
#         else:
#             error = True

#         if 'supervisor' in request.POST:
#             supervisor_id = request.POST.get('supervisor', '')
#         else:
#             error = True

#         if not error:
#             supervisor = Supervisor.objects.get(id = supervisor_id)
#             new_dev = Developer(name=name, login=login, password=password, my_supervisor=supervisor)
#             new_dev.save()

#             return HttpResponse("New developer is added.")
#         else:
#             return HttpResponse("An error is occured.")
#     else:
#         supervisors_list = Supervisor.objects.all()

#         return render(request, 'create_developer.html', {'supervisors_list': supervisors_list})


# using Django from
class FormInscription(forms.Form):
    name = forms.CharField(label="Name", max_length=30)
    login = forms.CharField(label="Login", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    supervisor = forms.ModelChoiceField(label="Supervisor", queryset=Supervisor.objects.all())


def create_developer(request):
    if request.POST:
        form = FormInscription(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            supervisor = form.cleaned_data['supervisor']

            new_developer = Developer(name=name, login=login, password=password, email='', my_supervisor=supervisor)
            new_developer.save()

            return HttpResponse("Developer added.")
        else:
            return render(request, 'create_developer.html', {'form': form})
            # return redirect(request.path)
    else:
        form = FormInscription()

        return render(request, 'create_developer.html', {'form': form})
