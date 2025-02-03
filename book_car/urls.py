from django.urls import path
from .views import car_list, reserve_car

urlpatterns = [
    path('', car_list, name='car_list'),
    path('reserve/<int:car_id>/', reserve_car, name='reserve_car'),
]

#<int:car_id> wskazuje, że parametr car_id musi być liczbą całkowitą (int). Django przekazuje tę wartość jako argument do widoku reserve_car.