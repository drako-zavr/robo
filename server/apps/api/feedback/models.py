from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Feedback(models.Model):
    """
    Модель заявки на курс
    """

    name = models.CharField("Имя", max_length=70, null=True, blank=False)
    phone = models.CharField("Телефон", max_length=11, null=True, blank=False)
    email = models.EmailField("Email", max_length=254, null=True, blank=False
    )
    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
        ordering = ["name"]
 

    def __str__(self):
        return self.name
