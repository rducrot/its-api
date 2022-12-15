from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField


class User(AbstractUser):

    username = None
    email = EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
