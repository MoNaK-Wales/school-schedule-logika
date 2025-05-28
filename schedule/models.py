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
    

class Schedule(models.Model):
    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    LESSON_NUMBERS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
    ]

    day = models.CharField(max_length=10, choices=DAYS_CHOICES)
    lesson_number = models.IntegerField(choices=LESSON_NUMBERS_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    lesson_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='schedules')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')


class Grade(models.Model):
    GRADES_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
    ]
    
    grade = models.IntegerField(choices=GRADES_CHOICES)
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.grade}"    
