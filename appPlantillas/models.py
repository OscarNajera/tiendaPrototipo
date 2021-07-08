from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre   = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    apodo    = models.CharField(max_length=20)
    correo   = models.CharField(max_length=50)
    contrasena =models.CharField(max_length=20)
    rfc = models.CharField(max_length=20)
    publico= models.BooleanField()
    def __str__(self):
         return self.nombre
    


class Eventos(models.Model):
    nombreEvento = models.CharField(max_length=20)
    fechaI = models.DateField(max_length=20)
    fechaF = models.DateField(max_length=20)
    #portrada = models.ImageField(default='null',upload_to="portadas")
    informacion = models.CharField(max_length=500)
    costo = models.CharField(max_length=20)
    horaInicio = models.CharField(max_length=20)
    horafinal = models.CharField(max_length=20)
    lugar = models.CharField(max_length=20)
    contacto = models.CharField(max_length=20)
    redeSociales = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="portadas", null=True)
    def __str__(self):
         return self.nombreEvento
    
    
    