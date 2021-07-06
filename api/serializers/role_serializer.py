from rest_framework import serializers
from ..models.role_model import RoleModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'