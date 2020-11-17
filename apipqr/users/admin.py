# from apipqr.users.models.client import Cliente
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from apipqr.users.models import users, client

# class UserAdmin(UserAdmin):
#     list_display =(
#         'email',
#         'telefono',
#         'identificacion',
#         'tipo_identificacion',
#         'email',
#         'is_client',
#         'is_verified'
#     )

# @admin.register(Cliente)
# class ClientAdmin(admin.ModelAdmin):
#     list_display=(
#         'user',
#         'descripcion'
#     )

# admin.site.register(users.User, UserAdmin)