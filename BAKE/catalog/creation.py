from .models import *
from django.core import management
from django.core.management import call_command


def initialize():
    if len(Product.objects.all()) == 0:
        management.call_command('loaddata', 'BAKE/data.json')