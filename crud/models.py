from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,primary_key=True)
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=100)