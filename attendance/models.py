from django.db import models

# Create your models here.


class Attendance(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    attendedClasses = models.IntegerField(editable=True, default=0)
    totalClasses = models.IntegerField(editable=True, default=0, null=True)
