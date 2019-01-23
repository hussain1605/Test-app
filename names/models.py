from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    surname = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name
