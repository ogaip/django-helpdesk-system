from django.contrib import admin

from .models import Dependencia


@admin.register(Dependencia)
class DependenciaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "dependencia_padre",
        "jefe",
        "activa",
    )
    list_filter = (
        "activa",
        "dependencia_padre",
    )
    search_fields = (
        "nombre",
        "jefe__username",
        "jefe__first_name",
        "jefe__last_name",
    )
    autocomplete_fields = (
        "dependencia_padre",
        "jefe",
    )
    ordering = ("nombre",)
    list_per_page = 25
    list_select_related = ("dependencia_padre", "jefe")
