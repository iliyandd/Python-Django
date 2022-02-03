from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    title = models.CharField(verbose_name="Title", max_length=43)
    content = models.TextField(verbose_name="Content")
    owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
