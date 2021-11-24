from django.contrib import admin
from django.urls import path

from Notes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    # path('about/', about, name="about"),
    # path('contacts/', contacts, name="contacts"),
]
