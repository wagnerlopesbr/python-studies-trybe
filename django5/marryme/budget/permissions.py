from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite acesso se for admin:
        if request.user.is_superuser:
            return True
        # Caso não seja admin e se o objeto tiver um atributo "user" igual ao request."user", permite acesso a quem faz a requisição:
        return obj.user == request.user
