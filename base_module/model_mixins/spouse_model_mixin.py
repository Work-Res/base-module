from django.db import models


class SpouseModelMixin(models.Model):
	spouse_last_name = models.CharField(max_length=190)
	spouse_first_name = models.CharField(max_length=190)
	spouse_middle_name = models.CharField(max_length=190)
	spouse_maiden_name = models.CharField(max_length=190)
	spouse_country = models.CharField(max_length=190)
	spouse_place_birth = models.CharField(max_length=190)
	spouse_dob = models.DateField()
	
	class Meta:
		abstract = True
