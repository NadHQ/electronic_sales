from django.http import HttpRequest
from rest_framework import permissions


class IsActiveUserPermission(permissions.BasePermission):
    """
    Is active user permission class
    """

    def has_permission(self, request: HttpRequest, view):
        return request.user.is_active and request.user.is_authenticated
