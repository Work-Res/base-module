from django.db import models


class CommissionerOathModelMixin(models.Model):

    declaration_place = models.CharField(
        max_length=190,
        null=True,
        blank=True,
    )

    oath_datetime = models.DateTimeField(
        null=True,
        blank=True,
        # validation=date_not_future,
        # auto_now_add=True
    )

    commissioner_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    # choice field?
    commissioner_designation = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    telephone_number = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    commissioner_signature = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
