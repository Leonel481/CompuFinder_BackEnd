from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length= 100, unique=True)
    def __str__(self) -> str:
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length= 100, unique=True)

    def __str__(self):
        return f'{self.name}'
    
class Category(models.Model):
    name = models.CharField(max_length= 100, unique=True)

    def __str__(self):
        return f'{self.name}'
    
class Product(models.Model):
    code = models.CharField(max_length= 50, unique=True,primary_key=True)
    company = models.ForeignKey('products.Company', on_delete=models.CASCADE, related_name='Product')
    brand = models.ForeignKey('products.Brand', on_delete=models.CASCADE, related_name='Product')
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, related_name='Product')
    name = models.CharField(max_length= 200,null=True, blank=True)
    link = models.CharField(max_length= 300, null=True, blank=True)
    image = models.CharField(max_length= 300, null=True, blank=True)
    price_usd = models.DecimalField(decimal_places = 2, max_digits=10)
    price_pen =models.DecimalField(decimal_places = 2, max_digits=10)
    discount_status = models.BooleanField(null=True, blank=True)
    discount = models.DecimalField(decimal_places = 2, max_digits=10,null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    datetime_scraper = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} | {self.category} | {self.brand} | {self.entity}'
    

class Stock(models.Model):
    code = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='Stock', to_field='code', db_column='code', default='999999999')
    stock = models.IntegerField(null=True, blank=True)
    datetime_scraper = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f'{self.code} | {self.stock}'
    
class Price(models.Model):
    code = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='Price', to_field='code', db_column='code', default='999999999')
    price_usd = models.DecimalField(decimal_places = 2, max_digits=10)
    price_pen =models.DecimalField(decimal_places = 2, max_digits=10)
    discount = models.DecimalField(decimal_places = 2, max_digits=10,null=True, blank=True)
    datetime_scraper = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f'{self.code} | {self.price_usd} | {self.price_pen}'