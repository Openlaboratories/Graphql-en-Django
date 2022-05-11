
from graphene_django import DjangoObjectType

from students.apps.usuarios.Grades.models import Grade


class GradeType(DjangoObjectType):
    class Meta:
        model = Grade
