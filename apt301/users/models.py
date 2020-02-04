from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        default=True,
        help_text=
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
