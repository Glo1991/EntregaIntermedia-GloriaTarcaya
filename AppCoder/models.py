from django.db import models
from django.contrib.auth.models import User

class TipoVehiculo(models.Model):

    name = models.CharField(max_length=150)
    

    def __str__(self):
        return f'{self.name}'

class Vehiculo(models.Model):

    marca=models.CharField(max_length=150)
    modelo=models.CharField(max_length=150)
    version = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.marca} - {self.modelo}  - {self.version} '

class Segmento(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'       

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
