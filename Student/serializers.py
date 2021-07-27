from django.db.models import fields
from rest_framework import serializers
from Student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('StudentId','StudentName','StudentPhno','StudentEmail')