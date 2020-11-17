from apipqr.users.models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

class ClienteAuth(BaseBackend):
    def authenticate(self, request, identificacion = None, password=None, **kwargs):
        try:
            cliente = Cliente.objects.get(identificacion = identificacion)
            user_cliente = User.objects.get(pk=cliente.user.id)
            if user_cliente.check_password(password):
                return cliente
            else:
                return None
        except Cliente.DoesNotExist:
            return None
        except User.DoesNotExist:
            return None