from django.urls import path
from .views import ProductListView, ProductDetailView, ProductNameListView, PriceListView

urlpatterns = [
    path('products-list/', ProductListView.as_view(), name='product-list'),
    path('<str:code>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', ProductNameListView.as_view(), name='product-name-search'),
    path('prices/', PriceListView.as_view(), name='price-product'),
]




#Consulta de productos en lista
# /api/v1/products/products-list/?offset=0&limit=10

#Consulta de productos en lista
# /api/v1/products/code/


#Consulta de productos con texto contenido en el nombre del producto
# /api/v1/products/search/?name=texto

#Consulta de productos en lista con filtros adicionales
# /api/v1/products/products-list/?company=name&category=name&brand=name&offset=0&limit=10

# Consulta de precios historicos
# /api/v1/prices/?code=code (sin paginacion)
# /api/v1/prices/?code=code&offset=0&limit=5 (con paginacion)