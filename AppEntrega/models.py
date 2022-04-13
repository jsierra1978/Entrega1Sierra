from django.db import models

# Create your models here.

class Lista_de_precios(models.Model):
    
    nombre_serv= models.CharField(max_length=40)
    precio= models.IntegerField()

    def __str__(self):
        return f"Servicio: {self.nombre_serv} - Precio: {self.precio}"


class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    dni= models.IntegerField()
    telefono= models.IntegerField()

class Profesional(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    especialidad= models.CharField(max_length=30)

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Especialidad {self.especialidad} "

class Turnos(models.Model):
    nombre= models.CharField(max_length=30)
    fecha_del_turno = models.DateField()  
    horario_asignado = models.IntegerField()