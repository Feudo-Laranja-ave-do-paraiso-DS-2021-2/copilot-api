from rest_framework.viewsets import ModelViewSet
from .models import User, Group
from .serializers import UserSerializers, GroupSerializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend #Filter Filtering


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero_celular', ]

class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializers
    queryset = Group.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['token', ]
