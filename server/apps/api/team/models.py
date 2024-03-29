from django.db import models
from django.utils.translation import gettext_lazy as _

class Teacher(models.Model):
    """
    Модель преподавателя
    """

    name = models.CharField(verbose_name=_("Имя"), max_length=255, null=True)
    surname = models.CharField(verbose_name=_("Фамилия"), max_length=255, null=True)
    photo = models.ImageField(verbose_name=_("Фотография"), blank=True, null=True)
    position = models.CharField(verbose_name=_("Должность"), max_length=255, null=True)
    social1 = models.CharField(verbose_name=_("Ссылка на соцсеть 1"), max_length=255, null=True)
    social2 = models.CharField(verbose_name=_("Ссылка на соцсеть 2"), max_length=255, null=True)
    info = models.CharField(verbose_name=_("Информация"), max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Преподаватель")
        verbose_name_plural = _("Преподаватели")
        ordering = ["name"]
 

    
