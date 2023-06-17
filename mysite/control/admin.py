from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .import models
admin.site.register(models.Empleado)
admin.site.register(models.Jornada)

class EmpleadoForm(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'turno', 'dias_de_trabajo', 'horario_entrada', 'horario_salida')
    list_fields = ['nombre']
    ordering = ['-Turno']
    

class JornadaForm(admin.ModelAdmin):
    list_display = ('id_empleado', 'fecha', 'tipo_marcacion')
    ordering = ['-Fecha']