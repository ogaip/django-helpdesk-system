from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
        User, on_delete=models.CASCADE, related_name='tickets_creados')
    asignado_a = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='tickets_asignados', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
