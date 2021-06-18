from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre   = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    apodo  = models.CharField(max_length=20)
    correo   = models.CharField(max_length=50)
    contrasena =models.CharField(max_length=20)
    rfc = models.CharField(max_length=20)
    publico= models.BooleanField()
    


