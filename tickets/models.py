from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_departments"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name

class Ticket(models.Model):
    class Status(models.TextChoices):
        ABIERTO = 'ABIERTO'
        EN_PROCESO = 'EN_PROCESO'
        CERRADO = 'CERRADO'

    class Priority(models.TextChoices):
        ALTA = 'ALTA'
        MEDIA = 'MEDIA'
        BAJA = 'BAJA'

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.ABIERTO)
    prioridad = models.CharField(
        max_length=20, choices=Priority.choices, default=Priority.MEDIA)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets_creados')
    asignado_a = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='tickets_asignados', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
