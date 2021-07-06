from django.urls import path, include
from rest_framework import routers
from .views import RoleViewSet, UserViewSet, DocumentCategoryViewSet, DocumentViewSet, UserDocumentViewSet


router = routers.DefaultRouter()
router.register(r'role', RoleViewSet, basename='role')
router.register(r'user', UserViewSet, basename='user')
router.register(r'document-category', DocumentCategoryViewSet, basename='document-category')
router.register(r'document', DocumentViewSet, basename='document')
router.register(r'user-document', UserDocumentViewSet, basename='user-document')

urlpatterns = [
	path('', include(router.urls))
]
