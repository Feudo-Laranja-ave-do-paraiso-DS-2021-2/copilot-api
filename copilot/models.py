from django.utils.crypto import get_random_string
from django.db import models


class Profile(models.Model):
    nome_completo = models.CharField(max_length=75, blank=True, )
    id_dispositivo = models.CharField(max_length=25, unique=True, )
    latitude = models.DecimalField(max_digits=15, decimal_places=10, )
    longitude = models.DecimalField(max_digits=15, decimal_places=10, )
    data_hora = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
       return self.nome_completo

class Group(models.Model):
    nome_grupo = models.CharField(max_length=25, )
    profiles = models.ManyToManyField(Profile, blank=True, )
    token = models.CharField(max_length=6, blank=True, null=True, editable=False, unique=True, )
    latitude_destino = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True )
    longitude_destino = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True )

    def set_token(self):
        string = get_random_string(6).upper()
        while Group.objects.filter(token=string):
            string = get_random_string(6).upper()
        self.token = string

    def save(self, *args, **kwargs):
        if not self.token:
            self.set_token()
        return super(Group, self).save(*args, **kwargs)

    def __str__(self):
       return self.nome_grupo
