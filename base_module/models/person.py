from django.db import models

from ..choices import MARITAL_STATUS, GENDER


class Person(models.Model):
	first_name = models.CharField(max_length=190)

	last_name = models.CharField(max_length=190)

	middle_name = models.CharField(
		max_length=190,
		blank=True,
		null=True)

	maiden_name = models.CharField(
		max_length=190,
		blank=True,
		null=True)

	marital_status = models.CharField(
		max_length=50,
		choices=MARITAL_STATUS)

	dob = models.DateField(
		#validations=date_not_future
	)

	country_birth = models.CharField(max_length=190)
	place_birth = models.CharField(max_length=190),
	gender = models.CharField(max_length=6, choices=GENDER)

	place_birth = models.CharField(max_length=190)

	gender = models.CharField(
		max_length=6,
		choices=GENDER)

	occupation = models.CharField(max_length=190)

	qualification = models.CharField(max_length=190)

	class Meta:
		verbose_name = 'Personal Details'
		verbose_name_plural = 'Personal Details'