from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Teacher(models.Model):
    """
    Модель преподавателя
    """

    name = models.CharField("Имя", max_length=254, null=True, blank=False)
    photo = models.CharField("Фото", max_length=500, null=True, blank=False)
    position = models.CharField("Должность", max_length=254, null=True, blank=False)
    social1 = models.CharField("Ссылка1", max_length=254, null=True, blank=False)
    social2 = models.CharField("Ссылка2", max_length=254, null=True, blank=False)
    info = models.CharField("Информация", max_length=254, null=True, blank=False)
    

    class Meta:
        verbose_name = _("Преподаватель")
        verbose_name_plural = _("Преподаватели")
        ordering = ["name"]
 

    def __str__(self):
        return self.name
