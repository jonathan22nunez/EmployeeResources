from ..models.role_model import RoleModel
from ..serializers.role_serializer import RoleSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class RoleViewSet(viewsets.ModelViewSet):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [DjangoFilterBackend]
