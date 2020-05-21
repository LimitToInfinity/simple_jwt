from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class AppleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Apple
        fields = ('id', 'url', 'name', 'color')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'password', 'email', 'secret_agent')
        extra_kwargs = { 'password': { 'write_only': True } }

    def create(self, validated_data):
        user = models.User.objects.create(
            username = validated_data['username'],
            password = make_password( validated_data['password'] ),
            email = validated_data['email'],
            secret_agent = validated_data['secret_agent']
        )

        user.save()
        
        return user