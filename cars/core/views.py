from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cars.car.models import Vehicle
from cars.core.forms import CarCommentForm
from cars.core.models import CarLike


def index(request):
    return render(request, 'index.html')


def comment_car(request, pk):
    car = Vehicle.objects.filter(pk=pk).get()

    form = CarCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.car = car
        comment.user = request.user
        comment.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required
def like_car(request, car_id):
    user_liked_car = CarLike.objects.filter(car=car_id, user=request.user.pk)

    if user_liked_car:
        user_liked_car.delete()
    else:
        CarLike.objects.create(
            car_id=car_id,
            user_id=request.user.pk,
        )

    return redirect(request.META['HTTP_REFERER'])




