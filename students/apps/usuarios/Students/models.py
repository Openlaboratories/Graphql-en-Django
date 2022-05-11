
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=45)
    photo = models.TextField()
    age = models.IntegerField()
