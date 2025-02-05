from django.db import models

class Car(models.Model):
    BODY_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('combi', 'Combi'),
        ('suv', 'SUV'),
    ]

    brand = models.CharField(max_length=100)
    production_year = models.IntegerField()
    body_type = models.CharField(
        max_length=10,
        choices=BODY_TYPE_CHOICES,
        default='sedan',
    )


    def __str__(self):
        return f'{self.brand} ({self.production_year}) - {self.get_body_type_display()}'
#new
class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reservation_date = models.DateField()

    def __str__(self):
        return f'Reservation for {self.car.brand} on {self.reservation_date}'

#get_body_type_display() -Użyłem tej metody, ponieważ jest to metoda wbudowana w Django pozwala zwrócić czytelną nazwę (np. "SUV") zamiast wartości zapisanej w bazie (np. "suv").
# Create your models here.
