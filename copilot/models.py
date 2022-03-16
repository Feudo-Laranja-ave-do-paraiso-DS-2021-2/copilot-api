from django.db import models


class User(models.Model):
    nome = models.CharField(max_length=32)
    mac_address = models.CharField(max_length=17, unique=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.nome

class Group(models.Model):
    nome = models.CharField(max_length=25)
    users = models.ForeignKey('User', on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=False)
    latitudeDest = models.DecimalField(max_digits=15, decimal_places=10)
    longitudeDest = models.DecimalField(max_digits=15, decimal_places=10)

    def __str__(self):
       return self.nome
