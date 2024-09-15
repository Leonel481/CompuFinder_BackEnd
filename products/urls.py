from django.urls import path
from .views import ProductListView, ProductDetailView, ProductNameListView, PriceListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<str:code>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/search/', ProductNameListView.as_view(), name='product-name-search'),
    path('prices/', PriceListView.as_view(), name='price-product'),
]


# /api/products/?company=name&category=name&brand=name&offset=0&limit=10
# /api/products/code/
# /api/products/search/?name=texto
# /api/prices/?code=code, /api/prices/?code=code&offset=0&limit=5