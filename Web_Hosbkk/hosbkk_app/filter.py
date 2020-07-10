import django_filters
from .models import *

class HospitalsFilter(django_filters.FilterSet):
    class Meta:
        model = Hospitals
        fields = '__all__'