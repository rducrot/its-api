from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import EmailField

from api.models import Contributor


class UserManager(BaseUserManager):
    """
    Custom user manager using email as identifier.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User using the email."""
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Use the private _create_user() to create a normal user."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Use the private _create_user() to create a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Custom User object. Uses email as identifier.
    """

    username = None
    email = EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']

    objects = UserManager()

    def is_author(self, project):
        """
        Return True if the current user is the author of the project.
        """
        try:
            instance = Contributor.objects.get(project=project, user=self)
            if instance.permission == Contributor.Permission.AUTHOR:
                return True
        except ValueError:
            # TODO
            pass
