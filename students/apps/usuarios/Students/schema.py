
from graphene_django import DjangoObjectType

from students.apps.usuarios.Students.models import Student


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
