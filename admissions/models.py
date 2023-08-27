# Create your models here.
from django.db import models
#from models import User
class Student(models.Model):
    name = models.CharField(max_length=1000)
    fathername = models.CharField(max_length=1000)
    classname = models.IntegerField()
    contact = models.CharField(max_length=15)

class Teacher(models.Model):
    name = models.CharField(max_length=1000)
    experience = models.IntegerField()
    subject= models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
