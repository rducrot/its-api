from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from authentication import serializers as auth_serializers


class UserViewSet(ModelViewSet):

    serializer_class = auth_serializers.UserSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(contributions=self.kwargs['project_pk'])
