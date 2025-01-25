from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'production_year', 'body_type')  # Wyświetlane kolumny
    list_filter = ('body_type', 'production_year')           # Filtry boczne
    search_fields = ('brand',)                               # Pole wyszukiwania


from django.contrib import admin

# Register your models here.
