from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm): #Tworzymy nową klasę ReservationForm, która dziedziczy po forms.ModelForm. ModelForm to specjalny typ formularza Django, który automatycznie tworzy pola na podstawie modelu bazy danych.
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'reservation_date']