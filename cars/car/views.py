from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from cars.car.forms import ManufacturerEditForm, ManufacturerDeleteForm, \
    VehicleAddForm, VehicleEditForm, VehicleDeleteForm
from cars.car.models import Manufacturer, Vehicle
from cars.core.forms import CarCommentForm, SearchCarForm
from cars.core.models import CarComment
from cars.core.utils import is_owner, add_likes_count, add_user_liked_photo

UserModel = get_user_model()


def catalog_view(request):
    search_form = SearchCarForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['car_name']

    cars = Vehicle.objects.all()

    if search_pattern:
        cars = Vehicle.objects.filter(manufacturer__name__icontains=search_pattern)

    if request.user.is_authenticated:
        user = request.user
        cars = [add_likes_count(car) for car in cars]
        cars = [add_user_liked_photo(car,user) for car in cars]

    paginator = Paginator(cars, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    count = len(cars)

    context = {
        'cars': cars,
        'search_form': search_form,
        'count': count,
        'user': False,
        'page_obj': page_obj,
    }

    return render(request, 'car/catalogue.html', context)


def catalog_user_view(request, pk):
    user = UserModel.objects.filter(pk=pk).get()
    cars = Vehicle.objects.filter(user_id=pk).all()
    cars = [add_likes_count(car) for car in cars]
    cars = [add_user_liked_photo(car,user) for car in cars]
    count = len(cars)

    context = {
        'cars': cars,
        'count': count,
        'user': user,
    }

    return render(request, 'car/catalogue_mycar.html', context)


@login_required
def catalog_user_like_view(request, pk):
    user = UserModel.objects.filter(pk=pk).get()
    cars = Vehicle.objects.all()
    cars = [add_likes_count(car) for car in cars]
    cars = [add_user_liked_photo(car,user) for car in cars]
    count = len(cars)

    context = {
        'cars': cars,
        'count': count,
        'user': user,
    }

    return render(request, 'car/catalogue_like.html', context)


def car_details_view(request, pk):
    car = Vehicle.objects.filter(pk=pk).get()
    comments = CarComment.objects.filter(car=pk).all()
    comment_form = CarCommentForm
    owner = UserModel.objects.filter(username=car.user).get()
    is_owner = False
    if request.user:
        is_owner = request.user == car.user

    context = {
        'car': car,
        'comment_form': comment_form,
        'is_owner': is_owner,
        'owner': owner,
        'comments': comments,
    }

    return render(request, 'car/car-details-view.html', context, )


@login_required
def car_add_view(request):
    if request.method == 'GET':
        form = VehicleAddForm()
    else:
        form = VehicleAddForm(request.POST, request.FILES)
    if form.is_valid():
        vehicle = form.save(commit=False)
        vehicle.user = request.user
        vehicle.save()
        return redirect('catalog')

    context = {
        'form': form,
    }

    return render(request, 'car/car-create-view.html', context, )


@login_required
def car_edit_view(request, pk):
    user = request.user
    car = Vehicle.objects.filter(pk=pk).get()

    if not is_owner(request, car):
        return redirect('catalog')

    if request.method == 'GET':
        form = VehicleEditForm(instance=car)
    else:
        form = VehicleEditForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('details car', pk=car.pk)

    context = {
        'form': form,
        'car': car,
        'owner': user.pk,
    }

    return render(request, 'car/car-edit-view.html', context )


@login_required
def car_delete_view(request, pk):
    user = request.user
    car = Vehicle.objects.filter(pk=pk).get()

    if not is_owner(request, car):
        return redirect('catalog')

    if request.method == 'GET':
        form = VehicleDeleteForm(instance=car)
    else:
        form = VehicleDeleteForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'car': car,
        'owner': user.pk,
    }

    return render(request, 'car/car-delete-view.html', context)


@login_required
def list_manufacturer(request):
    if not request.user.is_superuser:
        return render(request, 'index.html')

    allCars = Manufacturer.objects.all()

    context = {
        'allCars': allCars
    }
    return render(request, 'car/list-car-all-view.html', context, )


@login_required
def list_manufacturer_view(request, pk):
    if not request.user.is_superuser:
        return render(request, 'index.html')

    brand = Manufacturer.objects.filter(pk=pk).get()

    context = {
        'brand': brand
    }
    return render(request, 'car/list-car-one-view.html', context, )


@login_required
def list_manufacturer_edit(request, pk):
    if not request.user.is_superuser:
        return render(request, 'index.html')

    brand = Manufacturer.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ManufacturerEditForm(instance=brand)
    else:
        form = ManufacturerEditForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('all brand')

    context = {
        'form': form,
        'brand': brand,
    }

    return render(request, 'car/list-car-edit-view.html', context)


@login_required
def list_manufacturer_delete(request, pk):
    if not request.user.is_superuser:
        return render(request, 'index.html')

    brand = Manufacturer.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ManufacturerDeleteForm(instance=brand)
    else:
        form = ManufacturerDeleteForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('all brand')

    context = {
        'form': form,
        'brand': brand,
    }

    return render(request, 'car/list-car-delete-view.html', context)
