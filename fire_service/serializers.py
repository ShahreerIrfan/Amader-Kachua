from rest_framework import serializers
from .models import FireStation

class FireServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireStation
        fields = '__all__'  # Correct spelling of 'fields'
