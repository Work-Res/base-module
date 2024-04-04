from django.db import models
from ..choices import COMM_METHODS, POSTAL_PREFIX, YES_NO


class Contact(models.Model):

	contact_method = models.CharField(
		choices=COMM_METHODS,
		max_length=15
	)

	postal_prefix = models.CharField(
		choices=POSTAL_PREFIX,
		max_length=30,
		null=True,
		blank=True
	)

	contact_value = models.CharField(
		max_length=200
	)

	preferred_comm_method = models.CharField(
		verbose_name='Preferred method of contact?',
		choices=YES_NO,
		max_length=3
	)
	
	class Meta:
		verbose_name = 'Contact Details'
		verbose_name_plural = 'Contact Details'
