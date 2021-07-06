from django.db import models
from datetime import date
from .user_model import UserModel
from .document_model import DocumentModel


class UserDocumentModel(models.Model):
    status_types = ['Incomplete', 'In Progress', 'Completed', 'Expired']
    status = models.CharField(max_length=24)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    document = models.ForeignKey(DocumentModel, on_delete=models.CASCADE)
    created = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)

    @staticmethod
    def valid_status(status):
        for type in UserDocumentModel.status_types:
            if type == status:
                return True
        else:
            return False
