

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Reservation
from .forms import ReservationForm


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})


def reserve_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.car = car
            reservation.save()
            return redirect('car_list')
    else:
        form = ReservationForm()

    return render(request, 'reserve_car.html', {'form': form, 'car': car})