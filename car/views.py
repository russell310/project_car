from django_filters.views import FilterView
from .models import Car
from .filters import CarFilter


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
