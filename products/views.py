# from django.shortcuts import render
# import json
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework import status 
from .serializers import SerializerProduct, SerializerPrices
from .models import Product, Price
from .filters import ProductFilter, ProductNameFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    
class ProductNameListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductNameFilter

class PriceListView(ListAPIView):
    serializer_class = SerializerPrices
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        code = self.request.query_params.get('code', None)
        if not code:
            raise NotFound(detail="The 'code' parameter is required.")
        queryset = Price.objects.filter(code=code)
        if not queryset.exists():
            raise NotFound(detail="No prices found for the provided 'code'.")
        return queryset

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    lookup_field = 'code'
