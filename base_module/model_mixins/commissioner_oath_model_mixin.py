from django.db import models


class CommissionerOathModelMixin(models.Model):

    declaration_place = models.CharField(max_length=190)

    oath_datetime = models.DateTimeField(
        # validation=date_not_future,
        # auto_now_add=True
    )

    commissioner_name = models.CharField(max_length=255)

    # choice field?
    commissioner_designation = models.CharField(max_length=255)

    telephone_number = models.PositiveIntegerField()

    commissioner_signature = models.TextField()

    class Meta:
        abstract = True
