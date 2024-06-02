from django.test import TestCase, Client
from django.urls import reverse
from .factories import CarFactory
import xml.etree.ElementTree as ET


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


class CarListViewTest(TestCase):
    """
    Test case for the CarListView.

    This class contains tests to verify the functionality of the car list view,
    including pagination and XML export.
    """

    def setUp(self):
        self.client = Client()
        self.url = reverse('car_list')
        CarFactory.create_batch(15)

    def test_get_car_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car/list.html')
        self.assertEqual(len(response.context['cars']), 10)

    def test_export_to_xml(self):
        response = self.client.get(self.url, {'export': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="cars.xml"')

        tree = ET.fromstring(response.content)
        self.assertEqual(tree.tag, 'cars_list')
        self.assertEqual(len(tree.findall('car')), 15)

        for car_elem in tree.findall('car'):
            self.assertIsNotNone(car_elem.find('id').text)
            self.assertIsNotNone(car_elem.find('length').text)
            self.assertIsNotNone(car_elem.find('weight').text)
            self.assertIsNotNone(car_elem.find('velocity').text)
            self.assertIsNotNone(car_elem.find('color').text)


class CarFilterTest(TestCase):
    """
    Test case for the CarFilter.

    This class contains tests to verify the filtering functionality of the Car model.
    """

    def setUp(self):
        self.cars = CarFactory.create_batch(5)

    def test_filter_cars(self):
        car = self.cars[0]
        response = self.client.get(reverse('car_list'), {'color': car.color})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, car.color)

    def test_no_filter_cars(self):
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['cars']), 5)
