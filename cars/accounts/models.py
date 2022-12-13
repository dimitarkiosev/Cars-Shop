from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from cars.core.validators import validate_only_letters, validate_only_digits, validate_file_max_size_1mb


class CarsUser(auth_models.AbstractUser):
    MIN_LEN_FNAME = 2
    MAX_LEN_FNAME = 30
    MIN_LEN_LNAME = 2
    MAX_LEN_LNAME = 30
    MIN_LEN_PHONE = 9
    MAX_LEN_PHONE = 20

    first_name = models.CharField(
        max_length=MAX_LEN_FNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FNAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LNAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
    )

    phone = models.CharField(
        max_length=MAX_LEN_PHONE,
        validators=(
            validators.MinLengthValidator(MIN_LEN_PHONE),
            validate_only_digits,
        ),
        null=True,
        blank=True,
    )

    photo = models.ImageField(
        upload_to='account',
        validators=(
            validate_file_max_size_1mb,
        ),
        null=True,
        blank=True,
    )
