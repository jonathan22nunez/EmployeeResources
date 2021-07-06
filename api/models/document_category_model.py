from django.db import models


class DocumentCategoryModel(models.Model):
    category = models.CharField(max_length=255, unique=True)
