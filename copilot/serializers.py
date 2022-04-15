from dataclasses import fields
from rest_framework import serializers
from .models import Profile, Group


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'nome_completo', 'id_dispositivo', 'latitude', 'longitude', 'data_hora', )

        
class GroupSerializers(serializers.ModelSerializer):
    profiles = ProfileSerializers(many=True, required=False)
    class Meta:
        model = Group
        fields = ('id', 'nome_grupo', 'token', 'latitude_destino', 'longitude_destino', 'profiles', )
