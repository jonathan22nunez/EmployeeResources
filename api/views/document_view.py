from ..models import DocumentModel, UserModel, UserDocumentModel, RoleModel
from ..serializers.document_serializer import DocumentSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import json


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = DocumentModel.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = DocumentModel.valid_metadata(request.data['metadata'])
        if isinstance(result, str):
            return Response(result, status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'])
    def create_user_documents(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = DocumentModel.valid_metadata(request.data['metadata'], {"roles":list})
        if isinstance(result, str):
            return Response(result, status.HTTP_400_BAD_REQUEST)

        json_obj = json.loads(request.data['metadata'])

        result = RoleModel.validate_roles(json_obj['roles'])
        if isinstance(result, str):
            return Response(result, status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)

        for role in json_obj['roles']:
            UserDocumentModel.create_from_role(serializer.data['id'], role)

        return Response('test', status.HTTP_200_OK)
