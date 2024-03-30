import sys

from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from django.core.management.color import color_style
from django.core.exceptions import ImproperlyConfigured



style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'base_module'
    verbose_name = 'Base Module'

    def ready(self):
        sys.stdout.write(
            f' * default TIME_ZONE {settings.TIME_ZONE}.\n')
        if not settings.USE_TZ:
            raise ImproperlyConfigured('EDC requires settings.USE_TZ = True')
        sys.stdout.write(f' Done loading {self.verbose_name}.\n')
