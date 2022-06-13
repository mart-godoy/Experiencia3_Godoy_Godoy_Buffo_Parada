from django.db import models


# Create your models here.


#Modelo para el Usuario

class Usuario(models.Model):
    usuario = models.CharField(max_length=16, primary_key=True, verbose_name='Nombre de Usuario')
    nombre = models.CharField(max_length=40, verbose_name='Nombre Persona')
    password = models.CharField(max_length=30,verbose_name='Password')
    repcontraseña = models.CharField(verbose_name='Repetir contraseña', max_length=100, default='')
    correo = models.EmailField(max_length=100,verbose_name='Correo electronico')
    telefono = models.IntegerField(verbose_name='Telefono')

    def __str__(self):
        return self.usuario


#Modelo para el Envio

class Envio(models.Model):    
    rut = models.CharField(primary_key=True,max_length=10, verbose_name='Rut Persona')
    nombre = models.CharField(max_length=40, verbose_name='Nombre Persona')
    email = models.EmailField(max_length=100, verbose_name='Correo Electronico')
    phone = models.IntegerField(verbose_name='Numero Celular')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    comuna = models.CharField(max_length=50,verbose_name='Comuna')
    calle = models.CharField(max_length=100,verbose_name='Calle')
    casa = models.CharField(max_length=5,verbose_name='Numero Casa/Depto')

    def __str__(self):
        return self.rut