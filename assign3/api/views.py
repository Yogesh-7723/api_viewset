from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

class StudentCrud(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serialize = StudentSerializer(stu,many=True)
        return Response(serialize.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serialize = StudentSerializer(stu)
            return Response(serialize.data,status=status.HTTP_200_OK)
        

    def create(self,request):
        serialize = StudentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'success':'Data Successfully Created'},status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serialize = StudentSerializer(stu,data=request.data)
            serialize.save()
            return Response({'success':'Complete Update Successfull'},status=status.HTTP_426_UPGRADE_REQUIRED)

    def partial_update(self,request,pk=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serialize = StudentSerializer(stu,data = request.data,partial=True)
            return Response({'success':'Updation Completed'},status=status.HTTP_200_OK)

    def destroy(self,request,pk=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            stu.delete()
            return Response({'delete':"Student Data Delete Successsfully"},status=status.HTTP_202_ACCEPTED)

