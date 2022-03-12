from rest_framework import viewsets
from copilot.models import User
from copilot.serializers import UserSerializers
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializers
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['mac_address']
