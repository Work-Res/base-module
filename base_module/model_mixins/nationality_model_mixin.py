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

    previous_nationality = models.CharField(
        max_length=190,
        blank=True,
        null=True,
    )

    previous_botswana_id_no = models.IntegerField(
        blank=True,
        max_length=9,
    )

    class Meta:
        abstract = True
