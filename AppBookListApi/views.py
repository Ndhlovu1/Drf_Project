from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Test these inside Insomia 
@api_view(['POST','GET','PUT','PATCH'])
def books(request):
    return Response('list of the books', status=status.HTTP_200_OK)
    #return HttpResponse('List of the books', status=status.HTTP_200_OK)




