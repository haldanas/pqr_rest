# from apipqr.users.models.users import User
# from rest_framework import serializers
# from django.contrib.auth import password_validation,authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.validators import UniqueValidator
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# class UserModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'telefono',
#             'identificacion',
#             'tipo_identificacion',
#             'fecha_creacion',
#             'fecha_modificacion',
#             'email',
#             'is_client',
#             'is_verified'
#         )


# # class UserLoginSerializer(serializers.Serializer):
# #     username = serializers.CharField()
# #     password = serializers.CharField()

# #     def validate(self, data):
# #         user = authenticate(
# #             username=data['username'],
# #             password=data['password']
# #         )
# #         if not user:
# #             raise serializers.ValidationError('credenciales invalidas')
# #         if not user.is_verified:
# #             raise serializers.ValidationError('Usuario sin verificar')
# #         self.context['user'] = user
# #         return data

# #     def create(self, data):
# #         token, created = Token.objects.get_or_create(user=self.context['user']) 
# #         return self.context['user'], token.key



# # class UserSingnupSerializer(serializers.Serializer):

# #     username = serializers.CharField(
# #         validators = [UniqueValidator(queryset=User.objects.all())]
# #     )
# #     password = serializers.CharField(min_length = 4)
# #     #password_confirmation= serializers.CharField(min_length = 4)
# #     telefono = serializers.CharField()
# #     identificacion = serializers.CharField() 
# #     tipo_identificacion = serializers.CharField()
# #     email = serializers.EmailField()
    
# #     def validate(self,data):
# #         passwd = data['password']
# #         passwd_conf = data['password_confirmation']
# #         if passwd != passwd_conf:
# #             raise serializers.ValidationError('Claves no coinciden')
# #         password_validation.validate_password(passwd)
# #         return data 

# #     def create(self, data):
# #         data.pop('password_confirmation')
# #         user = User.objects.create_user(**data, is_verified=False)
# #         return user