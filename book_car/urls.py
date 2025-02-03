from django.urls import path
from .views import car_list, reserve_car

urlpatterns = [
    path('', car_list, name='car_list'),
    path('reserve/<int:car_id>/', reserve_car, name='reserve_car'),
]