from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from frenchie.auth_app.managers import FrenchieUserManager


class FrenchieUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 25
    USERNAME_MIN_LENGTH = 5

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
        ),
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = FrenchieUserManager()


class Customer(models.Model):
    NAME_MAX_LENGTH = 200
    NAME_MIN_LENGTH = 2

    user = models.OneToOneField(
        FrenchieUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        )
    )

    email = models.EmailField()

    picture = models.ImageField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name





