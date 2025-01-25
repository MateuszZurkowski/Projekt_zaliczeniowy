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

#get_body_type_display() - jest to metoda wbudowana w Django pozwala zwrócić czytelną nazwę (np. "SUV") zamiast wartości zapisanej w bazie (np. "suv").
from django.db import models

# Create your models here.
