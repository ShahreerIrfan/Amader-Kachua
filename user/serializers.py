from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = '__all__'  

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        

        password = validated_data.pop('password1')


        user_data = validated_data.pop('user')  
        user = User(**user_data)  
        user.set_password(password)  
        user.save()  

        validated_data.pop('password2', None)  
        user_profile = UserProfile.objects.create(user=user, **validated_data)

        return user_profile




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims (user_id is optional, already in payload)
        token['user_id'] = user.id

        # Include UserProfile ID
        try:
            user_profile = UserProfile.objects.get(user=user)
            token['user_profile_id'] = user_profile.id
        except UserProfile.DoesNotExist:
            token['user_profile_id'] = None  # Handle case where no UserProfile exists

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add user_id and UserProfile ID to the response
        data['user_id'] = self.user.id
        try:
            user_profile = UserProfile.objects.get(user=self.user)
            data['user_profile_id'] = user_profile.id
        except UserProfile.DoesNotExist:
            data['user_profile_id'] = None  # Handle case where no UserProfile exists

        return data
