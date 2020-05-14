import graphene
from graphene_django import DjangoObjectType
from .models import *


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class GradeType(DjangoObjectType):
    class Meta:
        model = Grade


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class CoursePerStudentType(DjangoObjectType):
    class Meta:
        model = CoursePerStudent


class Query(graphene.ObjectType):
    students = graphene.List(StudentType)
    grades = graphene.List(GradeType)
    courses = graphene.List(CourseType)
    courses_per_students = graphene.List(CoursePerStudentType)

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_grades(self, info, **kwargs):
        return Grade.objects.all()

    def resolve_courses(self, info, **kwargs):
        return Course.objects.all()

    def resolve_courses_per_students(self, info, **kwargs):
        return CoursePerStudent.objects.all()
