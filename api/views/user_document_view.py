from ..models.user_document_model import UserDocumentModel
from ..serializers.user_document_serializer import UserDocumentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class UserDocumentViewSet(viewsets.ModelViewSet):
    queryset = UserDocumentModel.objects.all()
    serializer_class = UserDocumentSerializer
    filter_backends = [DjangoFilterBackend]
