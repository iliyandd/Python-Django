from django.db import models

# Create your models here.

class Position(models.Model):
    position_name = models.CharField(max_length=100, verbose_name="Position", null=False)

    def __str__(self) -> str:
        return self.position_name


"""
Blank form:
1. First name
2. Last name
3. Email
4. Phone number
"""
class Blank(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    email = models.EmailField(null=False, verbose_name="Email")
    phone_number = models.CharField(max_length=20, verbose_name="Phone number")

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


"""
CV form:
1. Personal URL
2. Position
3. Technologies
4. Languages
5. Motivation
"""
class CV(Blank):
    url = models.CharField(max_length=150, verbose_name="Url", null=True, default=None)
    position = models.ForeignKey(Position, verbose_name="Position", on_delete=models.CASCADE)
    technologies = models.TextField(verbose_name="Technologies", null=False, default=None)
    languages = models.CharField(max_length=150, verbose_name="Languages", null=True)
    motivation = models.TextField(verbose_name="Motivation", null=False, default=None)


"""
Report form:
1. Issue
"""
class Issue(Blank):
    issue_area = models.TextField(verbose_name="Issue", null=False, default=None)


"""
Candidate model:
1. First name
2. Last name
3. Email
4. Phone number
"""