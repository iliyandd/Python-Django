from django.contrib import admin
from django.urls import path

from Notes.views import home, about, contacts, user_register, user_login, user_logout, display_notes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_register, name="user_register"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('home/<str:uid>/', home, name="home"),
    path('about/', about, name="about"),
    path('contacts/', contacts, name="contacts"),
    path('display-notes/', display_notes, name="display_notes")
]
