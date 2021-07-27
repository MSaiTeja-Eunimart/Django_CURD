from django.db import models
from django.db.models.base import Model

# Create your models here.

class Student(models.Model):
    StudentId = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=50)
    StudentPhno = models.CharField(max_length=10)
    StudentEmail = models.CharField(max_length=50)


