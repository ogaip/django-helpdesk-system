from django.db import models
from django.conf import settings

# Create your models here.

class Dependencia(models.Model):
    nombre = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="nombre",
    )

    dependencia_padre = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dependencias_hijas",
        verbose_name="dependencia superior",
    )

    jefe = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dependencias_a_cargo",
        verbose_name="jefe de dependencia",
    )

    activa = models.BooleanField(
        default=True,
        verbose_name="activa",
    )

    class Meta:
        ordering = ["nombre"]
        verbose_name = "dependencia"
        verbose_name_plural = "dependencias"

    def __str__(self):
        if self.dependencia_padre:
            return f"{self.dependencia_padre.nombre} > {self.nombre}"

        return self.nombre