from django.db import models


class Passport(models.Model):

	pass_no = models.CharField(
		verbose_name='Passport number',
		max_length=15)

	date_issued = models.DateField(
		verbose_name='Date of issue'
		# validation=date_not_future
	)

	place_issued = models.CharField(
		verbose_name='Country of issue',
		max_length=190)

	expiry_date = models.DateField(
		verbose_name='Date of expiry'
		# validation=date_not_past
	)

	nationality = models.CharField(
		max_length=190)

	photo = models.ImageField(
		upload_to='residence/%Y/%m'),

	class Meta:
		verbose_name = 'Passport'
