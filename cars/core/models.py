from django.contrib.auth import get_user_model
from django.db import models
from cars.car.models import Vehicle


UserModel = get_user_model()


class CarLike(models.Model):
    car = models.ForeignKey(
        Vehicle,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.car.model


class CarComment(models.Model):
    MAX_TEXT_LEN = 300

    text = models.CharField(
        max_length=MAX_TEXT_LEN,
        null=False,
        blank=False,
    )

    publication_date_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    car = models.ForeignKey(
        Vehicle,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.car.manufacturer