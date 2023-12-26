from django.db import models
from django.utils.translation import gettext_lazy as _

class Teacher(models.Model):
    """
    Модель преподавателя
    """

    name = models.CharField(_("Имя"), max_length=255, null=True)
    surname = models.CharField(_("Фамилия"), max_length=255, null=True)
    photo = models.ImageField(verbose_name=_("Фотография"), blank=True, null=True)
    position = models.CharField(_("Должность"), max_length=255, null=True)
    social1 = models.CharField(_("Ссылка1"), max_length=255, null=True)
    social2 = models.CharField(_("Ссылка2"), max_length=255, null=True)
    info = models.CharField(_("Информация"), max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Преподаватель")
        verbose_name_plural = _("Преподаватели")
        ordering = ["name"]
 

    
