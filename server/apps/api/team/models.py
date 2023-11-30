from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Teacher(models.Model):
    """
    Модель преподавателя
    """

    order = models.PositiveIntegerField(_("Порядок вывода"), null=True, blank=True)
    name = models.CharField(_("Имя"), max_length=255, null=True, blank=False)
    photo = models.ImageField(blank=True, null=True, verbose_name=_("Фотография"))
    position = models.CharField(_("Должность"), max_length=255, null=True, blank=False)
    social1 = models.CharField(_("Ссылка1"), max_length=255, null=True, blank=False)
    social2 = models.CharField(_("Ссылка2"), max_length=255, null=True, blank=False)
    info = models.CharField(_("Информация"), max_length=255, null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Преподаватель")
        verbose_name_plural = _("Преподаватели")
        ordering = ["name"]
 

    
