
from django.db import models

from students.apps.usuarios.Grades.models import Grade

class Course(models.Model):
    name = models.CharField(max_length=45)
    grades = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)
