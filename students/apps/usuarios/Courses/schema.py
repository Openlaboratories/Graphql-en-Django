
from graphene_django import DjangoObjectType

from students.apps.usuarios.Courses.models import Course


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
