from django.urls import path, include
from rest_framework import routers
from .views import RoleViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'role', RoleViewSet, basename='role')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
	path('', include(router.urls))
]
