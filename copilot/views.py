from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mac_address']
    def get(self, request, *args, **kwargs):
        emp = get_object_or_404(self.queryset, id=self.kwargs.get("pk"))
        serializer = UserSerializers(emp)
        return Response(serializer.data)
