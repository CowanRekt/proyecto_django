from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    titulo_academico = models.CharField(max_length=100)
    biografia = models.TextField()
    correo = models.EmailField()
    dedicacion = models.TextField()

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def str(self):
        return f'{self.nombres} {self.apellidos}'