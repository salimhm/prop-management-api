from django_filters import rest_framework as filters
from .models import Property

class PropertyFilter(filters.FilterSet):
    class Meta:
        model = Property
        fields = ['type']
        
    type = filters.CharFilter(field_name='type', lookup_expr='icontains')
    location = filters.CharFilter(field_name='address', lookup_expr='icontains')
    min_rental_cost = filters.NumberFilter(field_name='rental_cost', lookup_expr='lte')
    max_rental_cost = filters.NumberFilter(field_name='rental_cost', lookup_expr='gte')
