
from django.db import models

class Grade(models.Model):
    grade = models.DecimalField(max_digits=2, decimal_places=1)
