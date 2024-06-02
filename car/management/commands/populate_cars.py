from django.core.management.base import BaseCommand
from car.factories import CarFactory


class Command(BaseCommand):
    help = 'Populates the database with fake car data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='The number of cars to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for _ in range(count):
            CarFactory.create()
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} cars'))
