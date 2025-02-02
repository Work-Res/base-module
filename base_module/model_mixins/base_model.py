import socket

from django.db import models

from ..constants import BASE_MODEL_UPDATE_FIELDS
from ..model_fields import HostnameModificationField, UserField
from ..utils import get_utcnow


class BaseModel(models.Model):
    """Base model class for all models. Adds created and modified'
    values for user, date and hostname (computer).
    """

    get_latest_by = "modified"

    created = models.DateTimeField(blank=True, default=get_utcnow)

    modified = models.DateTimeField(blank=True, default=get_utcnow)

    user_created = UserField(
        max_length=50,
        blank=True,
        verbose_name="user created",
        help_text="Updated by admin.save_model",
    )

    user_modified = UserField(
        max_length=50,
        blank=True,
        verbose_name="user modified",
        help_text="Updated by admin.save_model",
    )

    hostname_created = models.CharField(
        max_length=60,
        blank=True,
        default=socket.gethostname,
        help_text="System field. (modified on create only)",
    )

    hostname_modified = HostnameModificationField(
        max_length=50, blank=True, help_text="System field. (modified on every save)"
    )

    objects = models.Manager()

    def save(self, *args, **kwargs):
        try:
            # don't allow update_fields to bypass these audit fields
            update_fields = kwargs.get("update_fields", None) + BASE_MODEL_UPDATE_FIELDS
            kwargs.update({"update_fields": update_fields})
        except TypeError:
            pass
        if not self.id:
            self.created = get_utcnow()
        self.modified = get_utcnow()
        self.hostname_created = self.hostname_created[:60]
        self.hostname_modified = self.hostname_modified[:50]
        super().save(*args, **kwargs)

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    class Meta:
        get_latest_by = "modified"
        ordering = (
            "-modified",
            "-created",
        )
        abstract = True
