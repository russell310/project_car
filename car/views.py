from django_filters.views import FilterView
from .models import Car
from .filters import CarFilter
import xml.etree.ElementTree as ET
from django.http import HttpResponse


# Create your views here.


class CarListView(FilterView):
    """
    View to display a paginated list of cars with filtering capabilities.
    """
    model = Car
    template_name = 'car/list.html'
    paginate_by = 10
    ordering = ('id',)
    context_object_name = 'cars'
    filterset_class = CarFilter

    def get(self, request, *args, **kwargs):
        if 'export' in request.GET:
            return self.export_to_xml()
        return super().get(request, *args, **kwargs)

    def export_to_xml(self):
        cars = self.filterset_class(self.request.GET, queryset=self.get_queryset()).qs
        root = ET.Element("cars_list")
        for car in cars:
            car_elem = ET.SubElement(root, "car")
            ET.SubElement(car_elem, "id").text = str(car.id)
            ET.SubElement(car_elem, "length").text = str(car.length)
            ET.SubElement(car_elem, "weight").text = str(car.weight)
            ET.SubElement(car_elem, "velocity").text = str(car.velocity)
            ET.SubElement(car_elem, "color").text = car.color
        tree = ET.ElementTree(root)
        response = HttpResponse(content_type='application/xml')
        response['Content-Disposition'] = 'attachment; filename="cars.xml"'
        tree.write(response, encoding='unicode')
        return response
