from django.db import models

# Create your models here.

#El modelo 'Usuarios' es para almacenar los datos de los que se logean
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.EmailField()
    registro = models.DateField()

#El modelo 'Temas' almacena los gustos de los usuarios. Se pueden editar a gusto
class Temas(models.Model):
    economia = models.CharField(max_length=50)
    juegos = models.CharField(max_length=50)
    naturaleza = models.CharField(max_length=50)
    internet = models.CharField(max_length=50)

#El modelo 'Staff' mostrara informacion de los admins de cada area
class Staff(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    area_control = models.CharField(max_length=50)

#class Curso(models.Model):
 #   nombre=models.CharField(max_length=50)
  #  comision=models.IntegerField()

 #   def __str__(self):
 #       return self.nombre+" "+str(self.comision)

