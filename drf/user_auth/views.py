from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from . models import registerUser
from .serializers import RegisterUserSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# register user 

@api_view(['GET', 'POST'])
def register_user(request):
    if request.method == 'GET':
        students = registerUser.objects.all()
        serializers = RegisterUserSerializer(students, many=True)
        return Response(serializers.data)

    if request.method == 'POST':
        print('inside post')
        serializers = RegisterUserSerializer(data=request.data)
        if registerUser.objects.filter(email=request.data['email']):
            return Response({"message": "User is already registered"})
        elif request.data['password'] != request.data['c_pass']:
            return Response({"message": "Passwords are not same"})
        else:
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'GET':
        return Response({'message':'Here You See your login status...'})

    if request.method == 'POST':
        
        try:
            if registerUser.objects.get(email=request.data['email'], password=request.data['password']):
                return Response({"message": "User Logged In"})
            
        except Exception as e:
            return Response({"message": "User is not registered"})
        
