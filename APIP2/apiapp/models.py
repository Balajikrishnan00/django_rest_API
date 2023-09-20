from rest_framework import serializers
from django.db import models


# Create your models here.

class Students(models.Model):
    name = models.TextField(max_length=100)
    age = models.IntegerField()
    m1 = models.IntegerField()
    m2 = models.IntegerField()
    m3 = models.IntegerField()

    def __str__(self):
        return f"{self.id}"

    @property
    def total(self):
        return int((self.m1 + self.m2 + self.m3))
        # return "%i" %(int(self.m1 + self.m2 + self.m3))

    @property
    def average(self):
        return round(self.total / 3, 2)

    @property
    def result(self):
        if self.m1 >= 35 and self.m2 >= 35 and self.m3 >= 35:
            # if (self.m1 == self.m2 == self.m3) >= 35:
            return "pass"
        else:
            return "fail"


class serializers_Student(serializers.ModelSerializer):
    class Meta:
        model = Students
        # fields = ['id', 'name', 'age', 'm1', 'm2', 'm3', 'total', 'average', 'result']
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("age is should be above 18")
        return data


