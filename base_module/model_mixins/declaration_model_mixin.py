from django.db import models


class DeclarationModelMixin(models.Model):

	declaration_fname = models.CharField(
		verbose_name='Declaration firstname',
		max_length=150
	)

	declaration_lname = models.CharField(
		verbose_name='Declaration lastname',
		max_length=150
	)

	declaration_date = models.DateField(
		#validation=date_not_future
	)

	signature = models.CharField(max_length=190)

	class Meta:
		abstract = True
