from django.db import models


class Passport(models.Model):
	pass_no = models.CharField(max_length=15)
	date_issued = models.DateField()
	place_issued = models.CharField(max_length=190)
	expiry_date = models.DateField()
	nationality = models.CharField(max_length=190)
	photo = models.ImageField(upload_to='residence/%Y/%m'),

	class Meta:
		verbose_name = 'Passport'
