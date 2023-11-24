from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TeamConfig(AppConfig):
    """Default app config"""

    name = "apps.api.team"
    verbose_name = _("Team")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
