import factory
from factory import Faker
from .models import Car


class CarFactory(factory.django.DjangoModelFactory):
    """
    Factory class for creating Car instances for testing purposes.

    This class uses the Factory Boy library to generate Car instances with random but realistic data
    for length, weight, velocity, and color. It leverages the Faker library to produce these random values.
    """

    class Meta:
        model = Car

    length = Faker('pyfloat', left_digits=1, right_digits=2, positive=True, min_value=3.0, max_value=5.0)
    weight = Faker('pyint', min_value=1000, max_value=2000)
    velocity = Faker('pyint', min_value=100, max_value=300)
    color = Faker('color_name')
