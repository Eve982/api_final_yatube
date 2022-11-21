from rest_framework import mixins, permissions, viewsets


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = "Нельзя изменять чужие данные."

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class CreateListModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass