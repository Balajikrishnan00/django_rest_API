from django.db import models


# Create your models here.
class Color(models.Model):
    color_name = models.CharField(max_length=30)

    def __str__(self):
        return self.color_name


class Person(models.Model):
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.CASCADE, related_name='color')
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


# This models for students
class Students(models.Model):
    roll_no = models.IntegerField()
    student_name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    behaviour = models.CharField(max_length=10)

    def __str__(self):
        return self.roll_no


# this model for Viewsets
class Employee(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_id = models.IntegerField()
    emp_age = models.IntegerField()

    def __str__(self):
        return self.emp_name
