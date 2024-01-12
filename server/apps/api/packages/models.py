from django.db import models
from django.utils.translation import gettext_lazy as _

class Package(models.Model):
    """
    Модель пакета
    """

    name = models.CharField(verbose_name=_("Название"), max_length=255, blank=False)
    price = models.CharField(verbose_name=_("Цена"), max_length=255, blank=False)
    desc = models.CharField(verbose_name=_("Описание"), max_length=255, blank=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Пакет")
        verbose_name_plural = _("Пакеты")
        ordering = ["id"]
 

    
