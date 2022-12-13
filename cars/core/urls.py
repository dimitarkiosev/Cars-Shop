from django.urls import path

from cars.core.views import index, like_car, comment_car

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:car_id>', like_car, name='like car'),
    path('comment/<int:pk>', comment_car, name='comment car'),
)
