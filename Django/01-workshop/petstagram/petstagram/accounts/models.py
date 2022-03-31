from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.accounts.managers import AppUserManager
from petstagram.validators.validators import only_letters_validator


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30,
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'username'

    objects = AppUserManager()


class Profile(models.Model):
    FIRST_MAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    FIRST_MAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2
    MIN_LEN_VALIDATOR_MESSAGE = 'Value must be over 2 chars!'

    MALE_GENDER = 'Male'
    FEMALE_GENDER = 'Female'
    DO_NOT_SHOW_GENDER = 'Do not show'

    GENDERS = [MALE_GENDER, FEMALE_GENDER, DO_NOT_SHOW_GENDER]

    first_name = models.CharField(
        max_length=FIRST_MAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_MAME_MIN_LENGTH, MIN_LEN_VALIDATOR_MESSAGE),
            only_letters_validator,
        ],

    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH, MIN_LEN_VALIDATOR_MESSAGE),
            only_letters_validator,
        ]
    )
    profile_picture = models.URLField()

    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=max(len(el) for el in GENDERS),
        choices=((g, g) for g in GENDERS),
        default=DO_NOT_SHOW_GENDER,
    )
    description = models.TextField(null=True, blank=True)

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
