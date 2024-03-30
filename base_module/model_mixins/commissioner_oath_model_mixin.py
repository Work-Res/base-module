from django.db import models


class CommissionerOathModelMixin(models.Model):
	commissioner_name = models.CharField(max_length=255)
	commissioner_designation = models.CharField(max_length=255)
	datetime = models.DateTimeField(auto_now_add=True)
	telephone_number = models.CharField(max_length=190)
	commissioner_signature = models.TextField()
	place_declaration = models.CharField(max_length=190)

	class Meta:
		abstract = True
