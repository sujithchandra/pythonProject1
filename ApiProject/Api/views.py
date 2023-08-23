#from django.shortcuts import render
from . models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Studentserializer

@api_view(['GET'])
def get_details(request):
    data = Student.objects.all()
    serializer = Studentserializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_details(request):
    serializer = Studentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_details(request, pk):
    data = Student.objects.get(Student, pk=pk)
    serializer = Studentserializer(data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(["DELETE"])
def delete_details(request, pk):
    data = Student.objects.get(pk=pk)
    data.delete()
    return Response(data)