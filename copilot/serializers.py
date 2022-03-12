from dataclasses import fields
from rest_framework import serializers
from copilot.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nome', 'mac_address', 'latitude', 'longitude', 'hora']