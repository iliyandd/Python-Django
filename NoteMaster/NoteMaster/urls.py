from django.contrib import admin
from django.urls import path

from Notes.views import home, about, contacts, user_register, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_register, name="user_register"),
    path('login/', user_login, name="user_login"),
    path('home/<str:uid>/', home, name="home"),
    path('about/', about, name="about"),
    path('contacts/', contacts, name="contacts")
]
