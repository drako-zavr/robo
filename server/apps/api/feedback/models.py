from django.db import models
from django.utils.translation import gettext_lazy as _

class Feedback(models.Model):
    """
    Модель заявки на курс
    """

    name = models.CharField("Имя", max_length=70, null=True)
    phone = models.CharField("Телефон", max_length=11, null=True)
    email = models.EmailField("Email", max_length=254, null=True)

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
        ordering = ["name"]
 

    def __str__(self):
        return self.name
