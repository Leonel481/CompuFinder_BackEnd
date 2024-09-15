from django.urls import path
from .views import ProductListView, ProductDetailView, ProductNameListView, PriceListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<str:code>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/search/', ProductNameListView.as_view(), name='product-name-search'),
    path('prices/', PriceListView.as_view(), name='price-product'),
]




#Consulta de productos en lista
# /api/products/?offset=0&limit=10

#Consulta de productos en lista
# /api/products/code/


#Consulta de productos con texto contenido en el nombre del producto
# /api/products/search/?name=texto

#Consulta de productos en lista con filtros adicionales
# /api/products/?company=name&category=name&brand=name&offset=0&limit=10

# Consulta de precios historicos
# /api/prices/?code=code (sin paginacion)
# /api/prices/?code=code&offset=0&limit=5 (con paginacion)