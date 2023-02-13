from rest_framework.permissions import BasePermission


class ProjectPermission(BasePermission):
    """
    Permissions for the project object.
    Only the author of the project can update and delete it.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve', 'create'):
            return True

        elif view.action in ('update', 'destroy'):
            if request.user.is_author(obj):
                return True


class ContributorPermission(BasePermission):
    """
    Permissions for the contributor object.
    Only the author of the linked project can update and delete it.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve'):
            return True

        elif view.action in ('create', 'destroy'):
            if request.user.is_author(obj.project):
                return True


class IssuePermission(BasePermission):
    """
    Permissions for the issue object.
    Only the author of the issue or the project can update and delete it.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve', 'create'):
            return True

        elif view.action in ('update', 'destroy'):
            if request.user.is_author(obj.project) or request.user == obj.author_user:
                return True


class CommentPermission(BasePermission):
    """
    Permissions for the comment object.
    Only the author of the comment or the project can update and delete it.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve', 'create'):
            return True

        elif view.action in ('update', 'destroy'):
            if request.user.is_author(obj.issue.project) or request.user == obj.author_user:
                return True
