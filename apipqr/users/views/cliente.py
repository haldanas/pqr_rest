from apipqr.users.models.cliente import Cliente
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from apipqr.users.serializers import (
    CrearCliente, 
    ClienteSerializer, 
    LoginCliente, 
    VerificacionClienteSerializer
)
    

class ClienteViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Cliente.objects.filter(is_verified=True)
    serializer_class = ClienteSerializer
    lookup_field = 'identificacion'
    #permission_classes = (IsAuthenticated)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginCliente(data=request.data)
        serializer.is_valid(raise_exception=True)
        cliente, token = serializer.save()
        data = {
            'cliente': ClienteSerializer(cliente).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def crear(self, request):    
        serializer = CrearCliente(data=request.data)
        serializer.is_valid(raise_exception=True)
        cliente = serializer.save()
        data = ClienteSerializer(cliente).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verificar(self, request):
        serializer = VerificacionClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Verificacion completada'}
        return Response(data, status=status.HTTP_200_OK)
