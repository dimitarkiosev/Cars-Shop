from cars.car.models import Vehicle
from cars.core.models import CarLike


def is_owner(request, obj):
    return request.user == obj.user


def get_car_by_name_and_username(car_pk, username):
    return Vehicle.objects.filter(pk=car_pk, user_id=username).get()


def add_likes_count(car):
    car.likes_count = car.carlike_set.count()
    return car


def add_user_liked_photo(car, user_pk):
    car.is_liked_by_user = False
    if CarLike.objects.filter(car=car.pk, user=user_pk).count() == 1:
        car.is_liked_by_user = True
    return car
