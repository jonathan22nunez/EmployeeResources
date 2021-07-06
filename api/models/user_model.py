from django.db import models
from .role_model import RoleModel


class UserModel(models.Model):
    status_types = ["Pending", "Active", "Terminated"]
    status = models.CharField(max_length=24)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)
    hire_date = models.DateField()
    termination_date = models.DateField(null=True, blank=True)

    @staticmethod
    def valid_status(status):
        for type in UserModel.status_types:
            if type == status:
                return True
        else:
            return False