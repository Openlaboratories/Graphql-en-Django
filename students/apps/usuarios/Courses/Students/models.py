
from django.db import models

from students.apps.usuarios.Courses.models import Course
from students.apps.usuarios.Students.models import Student

class CoursePerStudent(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    students = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
