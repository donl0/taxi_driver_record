from django.db import models


class RelativeOwnerPhone(models.Model):
    name = models.CharField(max_length=100, default="NULL", verbose_name="Имя", unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Родственник'
        verbose_name_plural = 'Родственники'