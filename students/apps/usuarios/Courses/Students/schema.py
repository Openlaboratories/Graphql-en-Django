
from graphene_django import DjangoObjectType

from students.apps.usuarios.Courses.Students.models import CoursePerStudent


class CoursePerStudentType(DjangoObjectType):
    class Meta:
        model = CoursePerStudent
