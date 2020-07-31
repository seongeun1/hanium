from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TourType
from .serializers import TourTypeSerializer

from django.shortcuts import render

# Create your views here.

@api_view(['GET'])
def tour_main(request):
    return Response("Hello")

@api_view(['GET'])
def select(request):
    tourType = TourType.objects.all()
    serializer = TourTypeSerializer(tourType, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def result(request):
    return Response("result")