
import graphene

from students.apps.usuarios.Courses.models import Course
from students.apps.usuarios.Grades.models import Grade
from students.apps.usuarios.Courses.Students.models import CoursePerStudent
from students.apps.usuarios.Students.models import Student

from students.apps.usuarios.Courses.schema import CourseType
from students.apps.usuarios.Grades.schema import GradeType
from students.apps.usuarios.Courses.Students.schema import CoursePerStudentType
from students.apps.usuarios.Students.schema import StudentType


# code from: https://stackoverflow.com/questions/49349689/how-to-return-customized-json-response-for-an-error-in-graphene-django-graphen
class APIException(Exception):

    def __init__(self, message, status_code=None):
        self.context = {}
        if status_code:
            self.context["status_code"] = status_code
        super().__init__(message)


class Query(graphene.ObjectType):
    students = graphene.List(StudentType)
    grades = graphene.List(GradeType)
    courses = graphene.List(CourseType)
    courses_per_students = graphene.List(CoursePerStudentType)

    def resolve_students(self, info, **kwargs):
        if (info.context.user.is_superuser):
            return Student.objects.all()
        elif (info.context.user.is_authenticated):
            return Student.objects.filter(user=info.context.user)
        else:
            raise APIException(
                "You must be logged in to access this data", 
                status_code=401
            )

    def resolve_grades(self, info, **kwargs):
        return Grade.objects.all()

    def resolve_courses(self, info, **kwargs):
        return Course.objects.all()

    def resolve_courses_per_students(self, info, **kwargs):
        return CoursePerStudent.objects.all()
