from enum import Enum
from django.core import validators
from django.db import models
from cars.accounts.models import CarsUser
from cars.core.model_mixins import ChoicesEnumMixin
from cars.core.validators import car_year_validator, validate_file_max_size_2mb


class Fuel(ChoicesEnumMixin, Enum):
    gasoline = 'Gasoline'
    diesel = 'Diesel'
    lpg = 'LPG'
    cng = 'CNG'
    electricity = 'Electricity'


class Manufacturer(models.Model):
    MIN_LEN_NAME = 2

    name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Vehicle(models.Model):
    MAX_LEN_MODEL = 50
    MIN_LEN_MODEL = 2
    MAX_VALUE_POWER = 1000

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=(
          validators.MinLengthValidator(MIN_LEN_MODEL),
        ),
        null=False,
        blank=False,
    )

    year = models.PositiveSmallIntegerField(
        validators=(
            car_year_validator,
        ),
        null=False,
        blank=False,
    )

    fuel = models.CharField(
        choices=Fuel.choices(),
        max_length=Fuel.max_len(),
        null=False,
        blank=False,
    )

    power = models.PositiveSmallIntegerField(
        validators=(
            validators.MaxValueValidator(MAX_VALUE_POWER),
        ),
        null=False,
        blank=False,
    )

    mileage = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    price = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    cimage = models.ImageField(
        upload_to='cars',
        validators=(
            validate_file_max_size_2mb,
        ),
        null=False,
        blank=False,
        verbose_name='Image'
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        CarsUser,
        on_delete=models.CASCADE,
    )

    publication_date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    def __str__(self):
        return f'{self.id}. {self.manufacturer} {self.model}'

    class Meta:
        ordering = ('-publication_date', 'manufacturer', 'model')