from django.db import models


# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=100)


class Person(models.Model):
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.CASCADE, related_name='color')
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name
