from django.db import models


class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=200)
    student_school = models.CharField(max_length=200)
    student_course = models.CharField(max_length=200)


    class Meta:
        db_table = 'student'
