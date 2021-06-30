from django.urls import path, include
from rest_framework import routers
from .views import RoleViewSet


router = routers.DefaultRouter()
router.register(r'role', RoleViewSet, basename='role')

urlpatterns = [
	path('', include(router.urls))
]
