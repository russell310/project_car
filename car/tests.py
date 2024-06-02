from django.test import TestCase
from .factories import CarFactory


class CarModelTest(TestCase):
    """
    Test case for the Car model.

    This class contains tests to verify the functionality of the Car model
    """

    def setUp(self):
        self.car = CarFactory()

    def test_car_str(self):
        self.assertEqual(
            str(self.car),
            f"{self.car.color} Car, L: {self.car.length}, W: {self.car.weight}, V: {self.car.velocity}",
        )

