from django.views.generic import ListView
from .models import Car


# Create your views here.


class CarListView(ListView):
    model = Car
    template_name = 'car/list.html'
    ordering = ('id',)
    context_object_name = 'cars'