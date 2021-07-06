from rest_framework import serializers
from ..models.document_model import DocumentModel


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = '__all__'