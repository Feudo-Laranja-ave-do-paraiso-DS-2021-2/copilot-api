from rest_framework.viewsets import ModelViewSet
from .models import Profile, Group
from .serializers import ProfileSerializers, GroupSerializers
from rest_framework.response import Response
from rest_framework.decorators import action
from itertools import chain


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()
    filterset_fields = ['id_dispositivo',]

class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializers
    queryset = Group.objects.all()
    filterset_fields = ['token', ]

    @action(methods=['post'], detail=True)
    def adicionar_profile(self, request, pk):
        profiles = request.data['ids']
        group = Group.objects.get(id=pk)
        old_profiles = group.profiles.all()
        all_profiles = chain(old_profiles, profiles)
        group.profiles.set(all_profiles)
        group.save()
        serializer = self.get_serializer(group)
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def retirar_profile(self, request, pk):
        profiles = request.data['ids']
        group = Group.objects.get(id=pk)
        for id in profiles:
            group.profiles.remove(id)
        group.save()
        serializer = self.get_serializer(group)
        return Response(serializer.data)
