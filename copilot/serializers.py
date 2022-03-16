from dataclasses import fields
from rest_framework import serializers
from .models import User, Group
#from django.db import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        """"
        nome = serializers.CharField(max_length=25)
        users = serializers.ForeignKey('User', on_delete=models.CASCADE, many=True)
        token = serializers.CharField(max_length=6, unique=False)
        latitudeDest = serializers.DecimalField(max_digits=15, decimal_places=10)
        longitudeDest = serializers.DecimalField(max_digits=15, decimal_places=10)
        """

