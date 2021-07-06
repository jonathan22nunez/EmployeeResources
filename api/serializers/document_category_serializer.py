from rest_framework import serializers
from ..models.document_category_model import DocumentCategoryModel


class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategoryModel
        fields = '__all__'