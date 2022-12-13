from django.contrib.auth.decorators import login_required
from django.urls import path, include
from cars.car.views import car_add_view, car_details_view, car_edit_view, car_delete_view, catalog_view, \
    list_manufacturer, list_manufacturer_view, list_manufacturer_edit, list_manufacturer_delete, catalog_user_view, \
    catalog_user_like_view

urlpatterns = (
    path('all/', list_manufacturer, name='all brand'),
    path('all/<int:pk>/', list_manufacturer_view, name='one brand'),
    path('all/<int:pk>/edit/', list_manufacturer_edit, name='edit brand'),
    path('all/<int:pk>/delete/', list_manufacturer_delete, name='delete brand'),
    path('list/', include([
        path('', catalog_view, name='catalog'),
        path('<int:pk>/', catalog_user_view, name='catalog user'),
        path('<int:pk>/like/', catalog_user_like_view, name='catalog like'),
    ])),
    path('create/', car_add_view, name='add car'),
    path('<int:pk>/', include([
        path('', car_details_view, name='details car'),
        path('edit/', car_edit_view, name='edit car'),
        path('delete/', car_delete_view, name='delete car'),
    ])),
)
