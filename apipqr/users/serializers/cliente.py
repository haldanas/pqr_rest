from django.contrib.auth.models import User
from django.db.models.query import InstanceCheckMeta
from rest_framework import serializers
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.crypto import get_random_string

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from apipqr.users.models import Cliente



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields = '__all__'
           


class CrearCliente(serializers.Serializer):
    
    usernames = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    
    telefono = serializers.CharField(max_length=50)
    identificacion = serializers.CharField(max_length=50)
    tipo_identificacion = serializers.CharField(max_length=50)
  
    def create(self, data):

        gen_password = get_random_string(length=32)

        user = User.objects.create_user(
            username=data['usernames'],
            password= gen_password,
            first_name=data['first_name'], 
            last_name=data['last_name'], 
            email=data['email']
        )

        cliente = Cliente.objects.create(
            user=user,
            telefono=data['telefono'],
            identificacion=data['identificacion'],
            tipo_identificacion=data['tipo_identificacion']
        )

        self.send_confirmation_email(cliente, user, gen_password)

        return cliente


    def send_confirmation_email(self, client, user, gen_password):
        # verification_token = self.gen_verification_token(client)
        subject = 'Valida tu cuenta @{}'.format(client.identificacion)
        from_email = settings.EMAIL_HOST_USER
        content = render_to_string(
            'emails/users/account_verification.html',
            {#'token': verification_token, 
            'password': gen_password,
            'cliente': client,
            'user': user
            }
        )
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()

    #def gen_verification_token(self, client):
    #    exp_date = timezone.now() + timedelta(days=3)
    #    payload = {
    #        'cliente': client.identificacion,
    #        'exp': int(exp_date.timestamp()),
    #        'type': 'email_confirmation'
    #    }
    #
    #    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    #
    #    return token.decode()


class LoginCliente(serializers.Serializer):

    identificacion = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def validate(self, data):
        cliente = authenticate(identificacion=data['identificacion'], password=data['password'])
        if not cliente:
            raise serializers.ValidationError('contraseña o usuario erroneos')
        if not cliente.is_verified:
            raise serializers.ValidationError('No has validado tu cuenta')
        self.context['cliente'] = cliente
        return data

    
    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context['cliente'].user)
        return self.context['cliente'], token.key


class VerificacionClienteSerializer(serializers.Serializer):
    """Account verification serializer."""
    """para verificar posiblemente despues
    de iniciar sesion la primera vez"""

    identification = serializers.CharField()
    password = serializers.CharField(max_length=50)
    confirm_password = serializers.CharField(max_length=50)

    def validate(self, data):
        client = Cliente.objects.get(identificacion=data['identification'])
        if not client:
            raise serializers.ValidationError('El usuario no existe')
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Las contraseñas no conciden')
        self.context['cliente'] = client
        self.context['password'] = data['password']
        return data

#    def validate_token(self, data):
#        """Verify token is valid."""
#        try:
#            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
#        except jwt.ExpiredSignatureError:
#            raise serializers.ValidationError('El link a espirado.')
#        except jwt.PyJWTError:
#            raise serializers.ValidationError('Token invalido 1')
#        if payload['type'] != 'email_confirmation':
#            raise serializers.ValidationError('Token invalido 2')
#
#        self.context['payload'] = payload
#        return data

    def save(self):
        """Update user's verified status."""
        cliente = self.context['cliente']
        user = User.objects.get(pk=cliente.user.id)
        cliente.is_verified = True
        user.set_password(self.context['password'])
        cliente.save()
        user.save()
        
