import json
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

    @staticmethod
    def valid_metadata(data, keys=None):
        valid = True
        json_obj = json.loads(data)

        if len(json_obj.keys()) < 1:
            valid = 'Metadata must have at least 1 key:value'
        elif keys:
            valid = DocumentModel.valid_metadata_keys(json_obj, keys)

        return valid

    @staticmethod
    def valid_metadata_keys(json_obj, keys):
        valid = True
        for key, value in keys.items():
            if key not in json_obj:
                valid = f'Metadata must have key: "{key}"'
                break
            elif not isinstance(json_obj[key], value):
                valid = f'"{key}" value must be of class <{value.__name__}>'
                break
            elif not json_obj[key]:
                valid = f'"{key}" value must not be blank'
                break
        return valid
