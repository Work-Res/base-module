from django.db import models

from identifier import UniqueNonCitizenIdentifierFieldMixin

from ..choices import GENDER, YES_NO
from ..model_mixins import BaseUuidModel


class Child(UniqueNonCitizenIdentifierFieldMixin, BaseUuidModel):

    first_name = models.CharField(max_length=150)

    last_name = models.CharField(max_length=150)

    age = models.PositiveIntegerField()

    gender = models.CharField(max_length=6, choices=GENDER)

    is_applying_residence = models.CharField(max_length=3, choices=YES_NO)

    class Meta:
        verbose_name = "Child"
        verbose_name_plural = "Children"
