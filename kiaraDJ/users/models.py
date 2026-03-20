from django.db import models

class Person(models.Model):

    class Rol(models.TextChoices):
        ESTUDIANT = 'Estudiant'
        PROFESSOR = 'Professor'

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    años = models.IntegerField()
    pais = models.CharField(max_length=30)
    rol = models.CharField(
        max_length = 30,
        choices = Rol,
        default = Rol.ESTUDIANT,
    )
