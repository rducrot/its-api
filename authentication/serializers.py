from django.contrib.auth import get_user_model
from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['pk', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
