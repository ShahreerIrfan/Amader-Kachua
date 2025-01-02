from django.shortcuts import render
from rest_framework import viewsets
from .models import Fire_Station
from .serializers import FireServiceSerializer
# Create your views here.

class FireStationViewset(viewsets.ModelViewSet):
    queryset = Fire_Station.objects.all()
    serializer_class = FireServiceSerializer
