from django.db import models


class DeclarationModelMixin(models.Model):

    declaration_fname = models.CharField(
        verbose_name="Declaration firstname",
        max_length=150,
        null=True,
        blank=True,
    )

    declaration_lname = models.CharField(
        verbose_name="Declaration lastname",
        max_length=150,
        null=True,
        blank=True,
    )

    declaration_date = models.DateField(
        # validation=date_not_future
        null=True,
        blank=True,
    )

    signature = models.CharField(
        max_length=190,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
