from ..models.document_category_model import DocumentCategoryModel
from ..serializers.document_category_serializer import DocumentCategorySerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class DocumentCategoryViewSet(viewsets.ModelViewSet):
    queryset = DocumentCategoryModel.objects.all()
    serializer_class = DocumentCategorySerializer
    filter_backends = [DjangoFilterBackend]