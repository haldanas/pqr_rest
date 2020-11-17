# Django
from django.db import models



"""MODEL"""
class Pqr(models.Model):

    user = models.ForeignKey('Cliente', on_delete=models.PROTECT)
    radicado = models.IntegerField(primary_key=True)
    TIPORAD=[
        ('PRE','Peticiones'),
        ('QUE','Quejas'),
        ('RES','Reclamos'),
        ('SOL','Sugerencias')
    ]
    tipo_radicado = models.CharField(max_length=50, choices=TIPORAD)
    comentario = models.CharField(max_length=50)
    TIPOESTADO=[
        ('NUE','Nuevo'),
        ('PRO','En proceso'),
        ('RES','Resuelto'),
        ('REC','Rechazado')
    ]
    estado = models.CharField(max_length=8, choices=TIPOESTADO)
    justificacion = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


    class meta:
        verbose_name='pqr'
        verbose_name_plural='pqrs'
        db_table= 'pqr'
