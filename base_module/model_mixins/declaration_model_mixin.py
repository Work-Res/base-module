from django.db import models


class DeclarationModelMixin(models.Model):
	date = models.DateField()
	signature = models.CharField(max_length=190)

	class Meta:
		abstract = True
