from django.urls import path
from .views import ProductListView, ProductDetailView, ProductNameListView, PriceListView, StockListView, ProductDiscountListView

urlpatterns = [
    path('products-list/', ProductListView.as_view(), name='product-list'),
    path('products-discount/', ProductDiscountListView.as_view(), name='product-discount'),
    path('product-detail/<str:code>', ProductDetailView.as_view(), name='product-detail'),
    path('product-name/', ProductNameListView.as_view(), name='product-name'),
    path('prices/<str:code_id>/', PriceListView.as_view(), name='price-list'),
    path('stock/<str:code_jd>/', StockListView.as_view(), name='stock-list'),
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
# /api/v1/prices/1234567/ (sin paginacion)
# /api/v1/prices/?code=code&offset=0&limit=5 (con paginacion)