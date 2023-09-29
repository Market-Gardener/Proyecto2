from django.db import models

class Pisina(models.Model):
    name = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Profesor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    last_name = models.CharField(max_length=30)

class Entregable(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    entregado = models.BooleanField()
