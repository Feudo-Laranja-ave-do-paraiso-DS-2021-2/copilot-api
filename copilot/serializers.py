from dataclasses import fields
from rest_framework import serializers
from .models import User, Group


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nome', 'mac_address', 'latitude', 'longitude', 'hora', )
        

class GroupSerializers(serializers.ModelSerializer):
    users = UserSerializers(many=True)
    
    class Meta:
        model = Group
        fields = ('id', 'nome', 'users', 'token', 'latitudeDest', 'longitudeDest', )

    def create(self, validated_data):
        users_data = validated_data.pop('users')
        group = Group.objects.create(**validated_data)
        for users_data in users_data:
            Group.objects.create(group=group, **user_data)
        return group
