from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()


class Grade(models.Model):
    grade = models.DecimalField(max_digits=2, decimal_places=1)


class Course(models.Model):
    name = models.CharField(max_length=45)
    grades = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)


class CoursePerStudent(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    students = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
