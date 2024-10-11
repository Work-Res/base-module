import sys

from django.apps import AppConfig as BaseAppConfig
from django.conf import settings
from django.core.management.color import color_style
from django.core.exceptions import ImproperlyConfigured

style = color_style()


class AppConfig(BaseAppConfig):
    name = "base_module"
    verbose_name = "Base Module"
    admin_site_name = "base_module_admin"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        sys.stdout.write(f" * default TIME_ZONE {settings.TIME_ZONE}.\n")
        if not settings.USE_TZ:
            raise ImproperlyConfigured("LOCHOIS requires settings.USE_TZ = True")
        sys.stdout.write(f" Done loading {self.verbose_name}.\n")
