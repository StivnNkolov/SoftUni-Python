from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE

from petstagram.accounts.models import Profile
from petstagram.validators.validators import only_letters_validator, validate_image_size

UserModel = get_user_model()


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

    user = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('user', 'name')


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

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id)
