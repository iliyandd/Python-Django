from django.contrib import admin
from django.urls import path

from Notes.views import home, about, contacts, user_register, user_login, user_logout, display_notes,\
                         delete_note, edit_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('register/', user_register, name="user_register"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('about/', about, name="about"),
    path('contacts/', contacts, name="contacts"),
    path('display-notes/', display_notes, name="display_notes"),
    path('delete-note/', delete_note, name="delete_note"),
    path('edit-note/', edit_note, name="edit_note"),
]
