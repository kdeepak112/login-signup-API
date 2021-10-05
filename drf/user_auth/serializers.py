from rest_framework import serializers
from .models import registerUser

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = registerUser
        fields = '__all__'