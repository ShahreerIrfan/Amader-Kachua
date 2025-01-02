from rest_framework import serializers
from .models import Fire_Station

class FireServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fire_Station
        fields = '__all__'  # Correct spelling of 'fields'
