from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from authentication.models import User
from authentication.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [AllowAny]

    serializer_class = UserSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return self.queryset

