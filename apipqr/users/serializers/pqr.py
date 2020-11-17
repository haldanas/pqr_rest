#DJANGO_REST
from rest_framework import serializers
#MODELOS
from apipqr.users.models.pqr import Pqr

"""SERIALIZERS"""
class PqrSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pqr
        fields = (
            #'user',
            'tipo_radicado',
            'comentario',
            'estado',
            'justificacion'
        )
        read_only_fields = (
            'radicado',
            'fecha_creacion',
            'fecha_modificacion',
            'reputation'
        )
