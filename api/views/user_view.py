from ..models.user_model import UserModel
from ..serializers.user_serializer import UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not UserModel.valid_status(request.data['status']):
            return Response('Invalid status. Must be of value Pending, Active, or Terminated', status.HTTP_400_BAD_REQUEST)

        if request.data['status'] == 'Terminated' and not request.data['termination_date']:
            return Response('Termination Date must be set for Status: Termination', status.HTTP_400_BAD_REQUEST)
        elif request.data['termination_date'] and request.data['status'] != 'Terminated':
            return Response('Status must be value Terminated if Termination Date is set.')

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if request.data['status'] == 'Terminated' and not request.data['termination_date']:
            return Response('Termination Date must be set for Status: Termination', status.HTTP_400_BAD_REQUEST)
        elif request.data['termination_date'] and request.data['status'] != 'Terminated':
            return Response('Status must be value Terminated if Termination Date is set.')

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
