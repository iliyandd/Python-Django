from django.contrib import admin

from Taskmanager.models import UserProfile, Project, Task, Supervisor , Developer

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Supervisor)
admin.site.register(Developer)
admin.site.register(Project)
admin.site.register(Task)