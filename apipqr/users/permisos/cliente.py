from rest_framework.permissions import BasePermission

from apipqr.users.models.pqr import Pqr

class IsAdmin(BasePermission):
    def has_object_permission(self,request,view,object):
        try:
            Pqr.objects.get(
                user= request.user,
                is_admin = True

            )
        except Pqr.DoesNotExist:
            return False
        return True