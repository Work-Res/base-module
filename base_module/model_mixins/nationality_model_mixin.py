from django.db import models


class NationalityModelMixin(models.Model):

    country_birth = models.CharField(
        max_length=190,
        blank=True,
        null=True,
    )

    place_birth = models.CharField(
        max_length=190,
        blank=True,
        null=True,
    )

    present_nationality = models.CharField(
        verbose_name="Current nationality",
        max_length=190,
        blank=True,
        null=True,
    )

    prev_nationality = (
        models.CharField(
            max_length=190,
            blank=True,
            null=True,
        ),
    )

    class Meta:
        abstract = True
