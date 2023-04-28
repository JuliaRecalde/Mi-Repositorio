from django.db import models

# Create your models here.


class Hotel(models.Model):
    #id_unico_hotel = models.AutoField()
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.EmailField()
    
class Reserva(models.Model):
    #id_unico_reserva = models.AutoField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    nro_huespedes = models.PositiveIntegerField()
    tipo_habitacion= models.CharField(max_length=200)
    precio_total = models.DecimalField(max_digits=8, decimal_places=2)
    estado_de_reserva = models.CharField(max_length=200)