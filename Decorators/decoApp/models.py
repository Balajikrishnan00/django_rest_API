from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)
