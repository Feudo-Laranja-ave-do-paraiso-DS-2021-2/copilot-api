from rest_framework.viewsets import ModelViewSet
from .models import User, Group
from .serializers import UserSerializers, GroupSerializers
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend #Filter Filtering
from rest_framework.decorators import action


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

    @action(methods=['post'], detail=True)
    def adicionar_user(self, request, pk):
        users = request.data['ids']
        group = Group.objects.get(id=pk)
        group.users.set(users)
        group.save()
        return HttpResponse('Ok, usuario(s) adicionado(s)!')

    @action(methods=['delete'], detail=True)
    def retirar_user(self, request, pk):
        users = request.data['ids']
        group = Group.objects.get(id=pk)
        for id in users:
            group.users.remove(id)
        group.save()
        return HttpResponse('Ok, usuario(s) removido(s)!')
