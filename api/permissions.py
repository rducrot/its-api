from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from api.models import Project, Issue, Comment, Contributor


class ProjectPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve', 'create'):
            return True

        elif view.action in ('update', 'destroy'):
            if request.user.is_author(obj):
                return True