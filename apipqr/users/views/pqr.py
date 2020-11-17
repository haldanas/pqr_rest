#DJANGO_REST
from rest_framework import viewsets
#SERIALIZERS
from apipqr.users.serializers.pqr import PqrSerializer
#MODELOS
from apipqr.users.models.pqr import Pqr

"""ViewSet implementa metodos y clases de los  mixins para el CRUD
esta interpreta el evento de http get,post,put,patch
https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py
https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py
"""
class PqrViewSet(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    queryset = Pqr.objects.all()
    serializer_class = PqrSerializer


