from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from authentication.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    View to create a new user.
    """
    permission_classes = [AllowAny]

    serializer_class = UserSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return self.queryset

