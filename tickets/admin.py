from django.contrib import admin
from .models import Ticket
# Register your models here.


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "descripcion",
        "status",
        "prioridad",
        "creado_por",
        "asignado_a",
        "fecha_creacion",
        "fecha_actualizacion",
    )
    list_filter = (
        "status",
        "prioridad",
        "creado_por",
        "asignado_a"
    )
    search_fields = (
        "titulo",
        "descripcion",
        "creado_por__username",
        "asignado_a__username"
    )
    ordering = (
        "-fecha_creacion",
    )
    readonly_fields = (
        "fecha_creacion",
        "fecha_actualizacion",
    )
