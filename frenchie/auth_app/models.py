from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models

from frenchie.auth_app.managers import FrenchieUserManager


class FrenchieUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
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
    user = models.OneToOneField(
        FrenchieUser,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    email = models.EmailField()

    picture = models.ImageField()

    def __str__(self):
        return self.name

