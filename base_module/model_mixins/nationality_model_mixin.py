from django.db import models


class NationalityModelMixin(models.Model):

	country_name = models.CharField(max_length=190)

	present_nationality = models.CharField(
		verbose_name='Current nationality',
		max_length=190)

	prev_nationality = models.CharField(max_length=190)

	class Meta:
		abstract = True
