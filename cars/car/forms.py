from django import forms
from cars.car.models import Manufacturer, Vehicle
from cars.core.models import CarLike, CarComment


class ManufacturerBaseForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ManufacturerAddForm(ManufacturerBaseForm):
    pass


class ManufacturerEditForm(ManufacturerBaseForm):
    pass


class ManufacturerDeleteForm(ManufacturerBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class VehicleBaseForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('manufacturer', 'model', 'year', 'fuel', 'power', 'mileage', 'price', 'cimage', 'description')


class VehicleAddForm(VehicleBaseForm):
    pass


class VehicleEditForm(VehicleBaseForm):
    pass


class VehicleDeleteForm(VehicleBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            CarLike.objects.filter(car=self.instance.id).delete()
            CarComment.objects.filter(car=self.instance.id).delete()
            self.instance.delete()

        return self.instance
