from dataclasses import fields
from rest_framework import serializers
from .models import User, Group


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'primeiro_nome', 'sobrenome', 'numero_celular', 'latitude', 'longitude', 'data_hora', )

class GroupSerializers(serializers.ModelSerializer):
    users = UserSerializers(many=True, required=False)
    class Meta:
        model = Group
        fields = ('id', 'nome_grupo', 'token', 'latitude_destino', 'longitude_destino', 'users', )
