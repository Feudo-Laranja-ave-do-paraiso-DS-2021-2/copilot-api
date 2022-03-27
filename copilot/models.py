from django.utils.crypto import get_random_string
from django.db import models


class User(models.Model):
    primeiro_nome = models.CharField(max_length=35, )
    sobrenome = models.CharField(max_length=35, )
    numero_celular = models.CharField(max_length=15, unique=True, )
    latitude = models.DecimalField(max_digits=8, decimal_places=6, )
    longitude = models.DecimalField(max_digits=9, decimal_places=6, )
    data_hora = models.DateTimeField(auto_now_add=True, )
    
    def __str__(self):
       return self.primeiro_nome

class Group(models.Model):
    nome_grupo = models.CharField(max_length=25, )
    users = models.ManyToManyField(User, blank=True, )
    token = models.CharField(max_length=6, blank=True, null=True, editable=False, unique=True, )
    latitude_destino = models.DecimalField(max_digits=8, decimal_places=6, )
    longitude_destino = models.DecimalField(max_digits=9, decimal_places=6, )

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
