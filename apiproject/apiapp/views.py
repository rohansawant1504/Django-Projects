from django.shortcuts import render
from .models import Employee
from .serializers import Employeeser


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class EmployeeViews(APIView):

    def get(self,r):
        edata = Employee.objects.all()  #orm in query form
        serdata = Employeeser(edata,many=True)   #json call fro convert into json
        return Response(serdata.data)

    def post(self,r):

        serobj = Employeeser(data = r.data)

        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)

        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)
