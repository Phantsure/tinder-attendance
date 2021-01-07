from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    subject = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    totalClasses = models.IntegerField(
        name="totalClasses",
        editable=True,
        default=0,
    )


class Enrolled(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True)
    classesAttended = models.IntegerField(
        name="classesAttended",
        editable=True,
        default=0,
    )
