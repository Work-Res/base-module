from django.db import models


class NationalityModelMixin(models.Model):

    country_birth = models.CharField(
        max_length=190,
        blank=True,
        null=True,
        verbose_name="Country of Birth",
    )

    place_birth = models.CharField(
        max_length=190,
        blank=True,
        null=True,
        verbose_name="Place of Birth",
    )

    present_nationality = models.CharField(
        verbose_name="Current nationality",
        max_length=190,
        blank=True,
        null=True,
    )

    previous_nationality = models.CharField(
        max_length=190,
        blank=True,
        null=True,
        verbose_name="Previous Nationality",
    )

    class Meta:
        abstract = True
