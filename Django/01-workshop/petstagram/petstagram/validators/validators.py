from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('The value must consist of only letters!')


def validate_image_size(image):
    file_size = image.file.size
    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError('Max file size is 5mb!')

