from django.db import models

from ..choices import PERMIT_TYPE


class PermitModelModelMixin(models.Model):
	permit_type = models.CharField(max_length=190) #, choices=PERMIT_TYPE)
	permit_no = models.CharField(max_length=190)
	date_issued = models.DateField()
	date_expiry = models.DateField()
	place_issue = models.CharField(max_length=190)

	class Meta:
		abstract = True
