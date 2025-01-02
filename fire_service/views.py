from django.shortcuts import render
from rest_framework import viewsets
from .models import FireStation
from .serializers import FireServiceSerializer
# Create your views here.

class FireStationViewset(viewsets.ModelViewSet):
    queryset = FireStation.objects.all()
    serializer_class = FireServiceSerializer
