from rest_framework import serializers
from .models import Student


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')  #('student_name', 'student_school', 'student_course')
