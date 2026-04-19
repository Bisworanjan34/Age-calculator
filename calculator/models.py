from django.db import models


# Create your models here.
class Calculator(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return self.year


class Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
