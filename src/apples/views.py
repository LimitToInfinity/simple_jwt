from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models, serializers

class ApplesView(viewsets.ModelViewSet):
    queryset = models.Apple.objects.all()
    serializer_class = serializers.AppleSerializer

class UsersView(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny,]