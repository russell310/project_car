from django.urls import path
from .views import CarListView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
]
