from rest_framework.viewsets import ModelViewSet
from .models import Profile, Group
from .serializers import ProfileSerializers, GroupSerializers
from django.http import HttpResponse
from rest_framework.decorators import action


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()
    filterset_fields = ['aplication_id', ]

class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializers
    queryset = Group.objects.all()
    filterset_fields = ['token', ]

    @action(methods=['post'], detail=True)
    def adicionar_profile(self, request, pk):
        profiles = request.data['ids']
        group = Group.objects.get(id=pk)
        group.profiles.set(profiles)
        group.save()
        return HttpResponse('Ok, usuario(s) adicionado(s)!')

    @action(methods=['delete'], detail=True)
    def retirar_profile(self, request, pk):
        profiles = request.data['ids']
        group = Group.objects.get(id=pk)
        for id in profiles:
            group.profiles.remove(id)
        group.save()
        return HttpResponse('Ok, usuario(s) removido(s)!')
