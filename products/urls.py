from django.urls import path
from .views import *

urlpatterns = [
    path('products-list/', ProductListView.as_view(), name='product-list'),
    path('products-discount/', ProductDiscountListView.as_view(), name='product-discount'),
    path('product-detail/<str:code>', ProductDetailView.as_view(), name='product-detail'),
    path('product-name/', ProductNameListView.as_view(), name='product-name'),
    path('prices/', PriceListView.as_view(), name='price-list'),
    path('stock/', StockListView.as_view(), name='stock-list'),
    path('company-list/', ProductCompany.as_view(), name='company-list'),
    path('brand-list/', ProductBrand.as_view(), name='brand-list'),
    path('category-list/', ProductCategory.as_view(), name='category-list'),
]




#Consulta de productos en lista
# /api/v1/products/products-list/?ordering=price_usd&offset=0&limit=10
# /api/v1/products/products-list/?price_usd_min=10&price_usd_max=50&offset=0&limit=10
## Consulta de productos en lista con filtros adicionales
# /api/v1/products/products-list/?company=name&category=name&brand=name&offset=0&limit=10

# descuentos
# /api/v1/products/products-discount/?discount_status=true

#Consulta de productos en lista
# /api/v1/products/product-detail/1234567


#Consulta de productos con texto contenido en el nombre del producto
# /api/v1/products/product-name/?name=texto

# Consulta de precios historicos
# /api/v1/products/prices/?code=1234567/ (sin paginacion)
# /api/v1/products/prices/?code=1234567&offset=0&limit=5 (con paginacion)


# Consulta de endpoint de tablas maestras
# /api/v1/products/company-list/?ordering=name        lista de empresas orden A-Z, para orden Z-A usar (?ordering=-name)
# /api/v1/products/brand-list/?ordering=name          lista de marcas orden A-Z, para orden Z-A usar (?ordering=-name)
# /api/v1/products/category-list/?ordering=name       lista de categorias de productos orden A-Z, para orden Z-A usar (?ordering=-name)