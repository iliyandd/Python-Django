from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30)
    content = models.TextField(verbose_name="Content")
    owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
