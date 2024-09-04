from django.db import models

from ..model_mixins import BaseUuidModel

from identifier import UniqueNonCitizenIdentifierFieldMixin


class Spouse(UniqueNonCitizenIdentifierFieldMixin, BaseUuidModel):
    last_name = models.CharField(max_length=190)
    first_name = models.CharField(max_length=190)
    middle_name = models.CharField(max_length=190, blank=True, null=True)
    maiden_name = models.CharField(max_length=190, blank=True, null=True)
    country = models.CharField(max_length=190)
    place_birth = models.CharField(max_length=190)
    dob = models.DateField()

    class Meta:
        verbose_name = "Spouse"
        verbose_name_plural = "Spouses"
