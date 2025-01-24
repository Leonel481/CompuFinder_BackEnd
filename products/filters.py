from django_filters import rest_framework as filters
from .models import Product, Price

class ProductFilter(filters.FilterSet):
    company = filters.CharFilter(field_name='company__name', lookup_expr='exact')
    category = filters.CharFilter(field_name='category__name', lookup_expr='exact')
    brand = filters.CharFilter(field_name='brand__name', lookup_expr='exact')
    # discount_status = filters.BooleanField(field_name='discount_status')

    class Meta:
        model = Product
        fields = ['company', 'category', 'brand']

class ProductNameFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']

# class PriceFilter(filters.FilterSet):
#     code = filters.CharFilter(field_name='code__iexact', lookup_expr='exact')

#     class Meta:
#         model = Price
#         fields = ['code']
