from django.db import models

class Pisina(models.Model):
    name = models.CharField(max_length=40)
    camada = models.IntegerField()

class Item(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=20)

class Users(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
