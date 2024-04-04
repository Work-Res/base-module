from django.db import models

from ..choices import GENDER, YES_NO


class ChildModelMixin(models.Model):

	child_first_name = models.CharField(
		max_length=150)

	child_last_name = models.CharField(
		max_length=150)

	child_age = models.PositiveIntegerField()

	gender = models.CharField(
		max_length=6,
		choices=GENDER)

	is_applying_residence = models.CharField(
		max_length=3,
		choices=YES_NO)

	class Meta:
		abstract = True
