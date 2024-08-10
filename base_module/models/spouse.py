from tabnanny import verbose
from django.db import models
from app.models import ApplicationBaseModel


class Spouse(ApplicationBaseModel):
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