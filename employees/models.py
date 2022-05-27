from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    department = models.CharField(max_length=100)
    salary = models.FloatField()
    birth_date = models.DateField(null=True, blank=True)