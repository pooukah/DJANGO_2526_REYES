from django.db import models

class Person(models.Model):

    class Rol(models.TextChoices):
        ESTUDIANT = 'EST', 'Estudiant'
        PROFESSOR = 'PRO', 'Professor'

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    años = models.IntegerField()
    pais = models.CharField(max_length=30)
    rol = models.CharField(
        max_length = 3,
        choices = Rol,
        default = Rol.ESTUDIANT,
    )
