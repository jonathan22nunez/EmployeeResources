from django.db import models

class RoleModel(models.Model):
	role = models.CharField(max_length=255)

	@staticmethod
	def is_unique(value):
		return not Role.objects.filter(role=value).exists()