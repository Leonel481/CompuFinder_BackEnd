import django_filters
from .models import Product, Price

class ProductFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(field_name='company__name', lookup_expr='exact')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='exact')
    brand = django_filters.CharFilter(field_name='brand__name', lookup_expr='exact')

    class Meta:
        model = Product
        fields = ['company', 'category', 'brand']

class ProductNameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']
