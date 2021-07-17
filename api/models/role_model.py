from django.db import models


class RoleModel(models.Model):
    role = models.CharField(max_length=255, unique=True)

    @staticmethod
    def validate_roles(roles):
        valid = True
        for role in roles:
            #query for role, check if exists
            if not RoleModel.objects.filter(role=role).exists():
                valid = f'Role: {role} does not exist'
                break
        return valid