# from django.shortcuts import render
# import json
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
from .serializers import *
from .models import *
from .filters import ProductFilter, ProductNameFilter
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication

from jwt_auth.authentication import CookieJWTAuthentication

class ProductListView(ListAPIView):
    """
    Filtrar la lista de productos segun los headers que se ingresen
    """
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [CookieJWTAuthentication] # Consumir el token de la cookie
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ["price_usd"]
    ordering = ["price_usd"]

class ProductDiscountListView(ListAPIView):
    """
    Devuelve los productos que tienen algún tipo de descuento
    discount_status: True
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SerializerProduct
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        queryset = Product.objects.all()  # Por defecto, traer todos los productos
        discount_status = self.request.query_params.get('discount_status')  # Obtener el parámetro de la URL
        if discount_status is not None:
            if discount_status.lower() in ['true', '1']:  # Convertir string a booleano
                queryset = queryset.filter(discount_status=True)
            elif discount_status.lower() in ['false', '0']:
                queryset = queryset.filter(discount_status=False)

        return queryset
    
class ProductNameListView(ListAPIView):
    """
    Api para consulta parciales, busca texto contenido en la columna
    """
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [CookieJWTAuthentication] # Consumir el token de la cookie
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductNameFilter

class PriceListView(ListAPIView):
    """
    Api para consulta de los precios historicos de un producto unico (precio, dscuento)
    """
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [CookieJWTAuthentication] # Consumir el token de la cookie
    permission_classes = [IsAuthenticated]
    queryset = Price.objects.all()
    serializer_class = SerializerPrices
    pagination_class = LimitOffsetPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = PriceFilter
    # lookup_field = 'code_id'

    def get_queryset(self):
        code = self.request.query_params.get('code', None)
        if not code:
            raise NotFound(detail="The 'code' parameter is required.")
        queryset = Price.objects.filter(code_id=code).order_by("datetime_scraper")
        if not queryset.exists():
            raise NotFound(detail="No prices found for the provided 'code'.")
        return queryset

class StockListView(ListAPIView):
    """
    Api para consulta de los precios historicos de un producto unico (precio, dscuento)
    """
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = SerializerStocks
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'code_id'

    # def get_queryset(self):
    #     code = self.request.query_params.get('code', None)
    #     if not code:
    #         raise NotFound(detail="The 'code' parameter is required.")
        
    #     # Filtra por la clave foránea code_id de la tabla Price
    #     queryset = Price.objects.filter(code_id=code)
        
    #     if not queryset.exists():
    #         raise NotFound(detail="No prices found for the provided 'code'.")
        
    #     return queryset

class ProductDetailView(RetrieveAPIView):
    """
    Api para consulta de datos actuales asociado a un solo producto (no historico).
    """
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [CookieJWTAuthentication] # Consumir el token de la cookie
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = SerializerProduct
    lookup_field = 'code'
    

class ProductCompany(ListAPIView):
    """
    Api para consultar la lista de empresas
    """

    authentication_classes = [CookieJWTAuthentication] # Consumir el token de la cookie
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = SerializerCompany
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name'] # Se permite ordenar de A-Z por name
    ordering = ['name'] # Orden por defecto A-Z

class ProductBrand(ListAPIView):
    """
    Api para consultar la lista de empresas
    """

    authentication_classes = [CookieJWTAuthentication] # Consumir el token de la cookie
    permission_classes = [IsAuthenticated]
    queryset = Brand.objects.all()
    serializer_class = SerializerBrand
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name'] # Se permite ordenar de A-Z por name
    ordering = ['name'] # Orden por defecto A-Z

class ProductCategory(ListAPIView):
    """
    Api para consultar la lista de empresas
    """

    authentication_classes = [CookieJWTAuthentication] # Consumir el token de la cookie
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = SerializerCategory
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name'] # Se permite ordenar de A-Z por name
    ordering = ['name'] # Orden por defecto A-Z