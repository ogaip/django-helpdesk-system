from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    class Rol(models.Model):
        ADMINSITRADOR = "ADMINISTRADOR", "Administrador"
        CAC = "CAC", "CAC"
        JEFE = "JEFE", "Jefe"
        TECNICO = "TECNICO", "Tecnico"

    dependencia = models.ForeignKey(
        "core.Dependencia",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        related_name="usuarios"
        verbose_name="dependencia"
    )
    rol = models.CharField(
        max_length=30,
        choices=Rol.choices,
        default=Rol.TECNICO,
        verbose_name="rol"
    )
    
    is_active = models.BooleanField(default=True)



