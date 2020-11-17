from django.db import models
from django.contrib.auth.models import User

"""MODEL"""
class Cliente(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    telefono = models.CharField(max_length=50)
    identificacion = models.CharField(unique=True,max_length=50)
    TIPOID=[
        ('CC','Cedula'),
        ('PAS','pasaporte'),
        ('PAE','P. extranjeria'),
    ]
    tipo_identificacion = models.CharField(max_length=50,choices=TIPOID)
    is_verified = models.BooleanField('Verificado', default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
        db_table= 'cliente'
