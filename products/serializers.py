from rest_framework import serializers
from .models import Product, Price, Stock, Company, Brand, Category

class SerializerProduct(serializers.ModelSerializer):
    code = serializers.CharField(max_length=20)
    company = serializers.CharField(max_length=100)
    brand = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=200)
    link = serializers.CharField(max_length=300)
    image = serializers.CharField(max_length=300)
    price_usd = serializers.FloatField()
    price_pen = serializers.FloatField()
    discount_status = serializers.BooleanField(default = False)
    discount = serializers.FloatField()
    stock = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('__all__')

class SerializerPrices(serializers.ModelSerializer):
    # price_usd = serializers.FloatField()
    # price_pen = serializers.FloatField()
    # discount = serializers.FloatField(allow_null=True)
    class Meta:
        model = Price
        fields = ['code', 'price_usd', 'price_pen', 'discount', 'datetime_scraper']

class SerializerStocks(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['code', 'stock', 'datetime_scraper']

class SerializerCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

class SerializerBrand(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']