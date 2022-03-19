from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE

from petstagram.validators.validators import only_letters_validator, validate_image_size


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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    ANIMAL_CHOICES = ['Cat', 'Dog', 'Bunny', 'Parrot', 'Fish', 'Other']

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=max(len(el) for el in ANIMAL_CHOICES),
        choices=((a, a) for a in ANIMAL_CHOICES)
    )

    date_of_birth = models.DateField(null=True, blank=True)

    user_profile = models.ForeignKey(
        Profile,
        on_delete=CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    DEFAULT_PHOTO_LIKES = 0

    photo = models.ImageField(
        upload_to='profiles',
        validators=(
            validate_image_size,
        )

    )
    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True
    )
    publication_time = models.DateTimeField(auto_now_add=True)

    likes = models.IntegerField(
        default=DEFAULT_PHOTO_LIKES,
    )

    def __str__(self):
        return str(self.id)
