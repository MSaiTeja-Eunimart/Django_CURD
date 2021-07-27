from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Student.models import Student
from Student.serializers import StudentSerializer

# Create your views here.


@csrf_exempt
def studentapi(request,id=0):
    if request.method=='GET':
        students = Student.objects.all()
        students_serializer = StudentSerializer(students,many=True)
        return JsonResponse(students_serializer.data,safe=False)

    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        students_serializer = StudentSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add")

    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(StudentId=student_data['StudentId'])
        students_serializer=StudentSerializer(student,data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        student=Student.objects.get(StudentId=id)
        student.delete() 
        return JsonResponse("Deleted Successfully",safe=False)


