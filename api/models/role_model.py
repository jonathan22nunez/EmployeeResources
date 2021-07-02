from django.db import models


class RoleModel(models.Model):
    role = models.CharField(max_length=255, unique=True)