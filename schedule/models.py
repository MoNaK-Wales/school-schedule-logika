from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.name
    

class Class(models.Model):
    number = models.IntegerField()
    letter = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.number}-{self.letter}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    students_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name