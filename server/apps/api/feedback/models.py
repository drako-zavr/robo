from django.db import models

# Create your models here.
class Feedback(models.Model):
    """
    Модель заявки на курс
    """

    name = models.CharField(_("Имя"), max_length=70, null=True, blank=False)
    phone = models.CharField(_("Телефон"), max_length=11, null=True, blank=False)
    email = models.EmailField(
        _("Email"), max_length=254, null=True, blank=False
    )
 

    def __str__(self):
        return self.name
