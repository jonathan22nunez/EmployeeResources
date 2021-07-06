from django.db import models
from datetime import date
from .document_category_model import DocumentCategoryModel


class DocumentModel(models.Model):
    status = models.CharField(max_length=24)
    title = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateField(default=date.today)
    document_category = models.ForeignKey(DocumentCategoryModel, on_delete=models.CASCADE)
    metadata = models.JSONField()
