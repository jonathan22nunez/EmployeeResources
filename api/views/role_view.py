from ..models.role_model import RoleModel
from ..serializers.role_serializer import RoleSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class RoleViewSet(viewsets.ModelViewSet):
	queryset = RoleModel.objects.all()
	serializer_class = RoleSerializer
	filter_backends = [DjangoFilterBackend]

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		if not RoleModel.is_unique(request.data['role']):
			return Response('Role already exists.', status=status.HTTP_400_BAD_REQUEST)

		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
