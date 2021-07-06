from rest_framework import serializers
from ..models.user_document_model import UserDocumentModel


class UserDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDocumentModel
        fields = '__all__'