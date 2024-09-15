from rest_framework import serializers
from .models import Product, Price

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
    price_usd = serializers.FloatField()
    price_pen = serializers.FloatField()
    discount = serializers.FloatField()

    class Meta:
        model = Price
        fields = ['price_usd', 'price_pen', 'discount', 'datetime_scraper']