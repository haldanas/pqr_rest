# # from django.http import JsonResponse
# # from django.http import request
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from apipqr.users.models.users import User
# # from apipqr.users.serializers.serializers import CreateUserSerializer, UserSerializer

# # @api_view(['GET'])
# # def lista_users (request):
# #     usuarios = User.objects.all()
# #     data=[]
# #     for usuario in usuarios:
# #         serializer =  UserSerializer(usuario, many=True)
# #         data.append(serializer.data)  
# #     return Response(data)

# # @api_view(['POST'])
# # # def create_users(request):
# #     serializer = CreateUserSerializer(data=request.data)
# #     serializer.is_valid(raise_exception=True)
# #     data = serializer.data
# #     usuaio = User.objects.create(**data)
# #     return Response(UserSerializer(usuaio).data) 

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status

# from apipqr.users.serializers import (
#     UserLoginSerializer,
#     UserModelSerializer,
#     UserSingnupSerializer
#     )

# class UserLoginAPIView(APIView):

#     def post(self,request, *args,  **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user, token = serializer.save()
#         data={
#             'user':UserModelSerializer(user).data,
#             'acces_token':token
#         }
#         return Response(data, status=status.HTTP_201_CREATED)

# class UserSingnupAPIView(APIView):
#     def post(self,request, *args,  **kwargs):
#         serializer = UserSingnupSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         data= UserModelSerializer(user).data
#         return Response(data, status=status.HTTP_201_CREATED)