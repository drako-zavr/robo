from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PackagesConfig(AppConfig):
    """Default app config"""

    name = "apps.api.packages"
    verbose_name = _("Packages")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
