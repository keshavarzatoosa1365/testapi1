from rest_framework import permissions
# from .models import myuser

# class IsOwner(permissions.BasePermission):
#     def has_permission(self,request,view):
#         try:
#             user=myuser.objects.get(email=request.query_parms['email'])
#         except:
#             return False

#         if request.user.is_staff:
#             return True
#         if request.user==user:
#             return True
#         else:
#             return False        