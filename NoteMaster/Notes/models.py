from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100, default="Empty title")
    content = models.TextField(verbose_name="Content")
    owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)