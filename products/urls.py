from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductAPI.as_view()),
    path('products/<int:pk>/', ProductAPI.as_view()),
]
