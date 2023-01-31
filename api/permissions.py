from rest_framework.permissions import BasePermission


class ProjectPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve', 'create'):
            return True

        elif view.action in ('update', 'destroy'):
            if request.user.is_author(obj):
                return True


class ContributorPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve'):
            return True

        elif view.action in ('create', 'destroy'):
            if request.user.is_author(obj.project):
                return True


class IssuePermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve', 'create'):
            return True

        elif view.action in ('update', 'destroy'):
            if request.user.is_author(obj.project) or request.user == obj.author_user:
                return True


class CommentPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve', 'create'):
            return True

        elif view.action in ('update', 'destroy'):
            if request.user.is_author(obj.issue.project) or request.user == obj.author_user:
                return True
