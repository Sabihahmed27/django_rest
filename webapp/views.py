from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse  # to request using HTTP data
from django.shortcuts import get_object_or_404      # we get 404 when the object doesnot exist
from rest_framework.views import APIView        #APIViews are used to return API data
from rest_framework.response import Response    #to get Status response
from rest_framework import status   #to get status
from .models import employees  #
from .serializers import employeesSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser




class employeeList(APIView):            #Class based view
    def get(self,request):              #to return all employees
        employees1 = employees.objects.all()  #It will take all the objects then and convert to JSON
        serializer = employeesSerializer(employees1,many=True)          #by passing all object all will be serialized, thats what the keyword 'many=True' means
        return Response(serializer.data)


    def post(self,request):
        emp = request.data.get('employee')
        # Create an article from the above data
        serializer = employeesSerializer(data='emp')
        if serializer.is_valid(raise_exception=False):
            employee_saved = serializer.save()
            return Response(employee_saved.data)
        else:
            return Response({"failure"})
        # return Response({"success": "Article '{}' created successfully".format(employee_saved.data)})

        # data = JSONParser().parse(request)
        # serializer = employeesSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
