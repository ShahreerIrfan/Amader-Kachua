from rest_framework import serializers
from .models import Doctor, Contact, Availability

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['phone', 'email']

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['day', 'time']

class DoctorSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    availability = AvailabilitySerializer(many=True)  # Remove 'source' argument
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'location', 'contact', 'availability', 'photo']
