from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

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
        fields = '__all__'  # Including all fields from UserProfile model and password fields

    def validate(self, data):
        """
        Ensure that password1 and password2 are the same.
        """
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        """
        Create a new user and user profile.
        """
        # Remove password1 and password2 from validated_data before passing to UserProfile
        password = validated_data.pop('password1')

        # Create the User instance
        user_data = validated_data.pop('user')  # Remove user data for creating user
        user = User(**user_data)  # Create the user instance
        user.set_password(password)  # Hash the password before saving
        user.save()  # Save the user instance

        # Now create the UserProfile instance with remaining validated data
        validated_data.pop('password2', None)  # Ensure password2 is not passed to UserProfile
        user_profile = UserProfile.objects.create(user=user, **validated_data)

        return user_profile
