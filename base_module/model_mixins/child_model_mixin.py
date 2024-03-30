from django.db import models

from ..choices import GENDER, YES_NO


class ChildModelMixin(models.Model):
	name = models.CharField(max_length=190)
	age = models.IntegerField()
	gender = models.CharField(max_length=10, choices=GENDER)
	is_applying_residence = models.CharField(max_length=10, choices=YES_NO)

	class Meta:
		abstract = True
