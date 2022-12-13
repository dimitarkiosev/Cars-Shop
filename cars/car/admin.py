from django.contrib import admin
from cars.car.models import Manufacturer, Vehicle


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    fields = ('manufacturer', 'model','year', 'fuel', 'power', 'mileage', 'price', 'cimage', 'description', 'user',)
    list_display = ('id', 'manufacturer', 'model', 'price', 'year', 'fuel', 'user', )
    list_filter = ('year', 'fuel',)
    search_fields = ('manufacturer',)
    ordering = ('manufacturer', 'model',)
    list_per_page = 20

