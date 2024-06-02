import django_filters
from .models import Car


class CarFilter(django_filters.FilterSet):
    """
    Filter class for the Car model.

    This class provides filtering capabilities for the Car model based on its attributes:
    length, weight, velocity, and color.
    """

    class Meta:
        model = Car
        fields = ['length', 'weight', 'velocity', 'color']
