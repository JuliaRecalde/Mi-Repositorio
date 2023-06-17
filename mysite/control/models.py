from django.db import models

# Create your models here.
from django.db import models

class Empleado(models.Model):
    TURNOS_CHOICES = (
        ('D', 'Día'),
        ('T', 'Tarde'),
        ('N', 'Noche'),
    )
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    dias_de_trabajo = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    horario_entrada = models.TimeField()
    horario_salida = models.DateTimeField()
    
    #cambios
    activo = models.BooleanField(default=True)
    telefono = models.CharField(max_length=20, blank=True)

    #def __str__(self):
    #    return self.nombre


class Jornada(models.Model):
    TIPO_MARCACION_CHOICES = (
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    )
    
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tipo_marcacion = models.CharField(max_length=7, choices=TIPO_MARCACION_CHOICES)

    #def __str__(self):
     #   return f"{self.empleado.nombre} - {self.fecha}"
