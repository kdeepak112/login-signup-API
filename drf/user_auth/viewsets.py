from rest_framework import viewsets
from . import models
from . import serializers

class registerViewset(viewsets.ModelViewSet):
    queryset = models.registerUser.objects.all()
    serializer_class = serializers.RegisterUserSerializer