from django.contrib import admin

from students.apps.usuarios.Courses.Students.models import CoursePerStudent
from students.apps.usuarios.Courses.models import Course
from students.apps.usuarios.Grades.models import Grade
from students.apps.usuarios.Students.models import Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(CoursePerStudent)
