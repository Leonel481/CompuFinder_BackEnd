from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status 
from .serializers import *
from .models import *

# class ProductAPI(APIView):
#     # serializer_class = List_of_product_Serializer

#     def get(self, request):
#         productos = Product.objects.all()
#         serializer = List_of_product_Serializer(productos, many = True)
        
#         return Response({
#                         'status': 'success',
#                         'data': serializer.data
#                         }, status=status.HTTP_200_OK
#                         )

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = List_of_product_Serializer
    pagination_class = LimitOffsetPagination

    def get(self, request):
        return self.list(request)