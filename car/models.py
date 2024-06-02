from django.db import models


# Create your models here.


class Car(models.Model):
    """
    Represents a car with specific attributes such as length, weight, velocity, and color.

    Attributes:
       length (float): The length of the car in meters.
       weight (float): The weight of the car in kilograms.
       velocity (float): The velocity of the car in meters per second.
       color (str): The color of the car.
    """
    length = models.FloatField()
    weight = models.FloatField()
    velocity = models.FloatField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.color} Car, L: {self.length}, W: {self.weight}, V: {self.velocity}"
