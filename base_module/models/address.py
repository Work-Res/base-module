from django.db import models


class Address(models.Model):

	country = models.CharField(max_length=190)

	town = models.CharField(max_length=190)

	street = models.TextField(blank=True)

	box_no = models.CharField(max_length=190)

	plot_no = models.CharField(
		blank=True,
		null=True,
		max_length=100)

	post_office_location = models.CharField(max_length=190)

	class Meta:
		verbose_name = 'Address'
