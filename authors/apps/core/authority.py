from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
   def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
           return True
       else:
           return obj.author == request.user


class IsBookmarOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user      