from datetime import date
from cars.car.models import Vehicle, Manufacturer


def create_car_for_user(user, count=2):
    audi = Manufacturer(name="Audi")
    audi.save()

    result = [Vehicle(
        model = f'A{3+i}',
        year = f'1998',
        fuel = 'diesel',
        power = 140,
        mileage = 150000,
        price = 10000,
        cimage = f'testPic.jpg',
        description = 'top condition',
        user = user,
        manufacturer_id = audi.pk,
        publication_date = date(2015 + i, (1 + i) % 12, (1 + i) % 28),
    ) for i in range(count)]

    [p.save() for p in result]

    return result



