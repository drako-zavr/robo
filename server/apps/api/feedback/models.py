from django.db import models
from django.utils.translation import gettext_lazy as _

class Feedback(models.Model):
    """
    Модель заявки на курс
    """

    name = models.CharField(verbose_name=_("Имя"), max_length=100, null=True)
    phone = models.CharField(verbose_name=_("Телефон"), max_length=11, null=True)
    email = models.EmailField(verbose_name=_("Email"), max_length=255, null=True)

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
        ordering = ["name"]
 

    def __str__(self):
        return self.name
