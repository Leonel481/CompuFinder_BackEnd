from django.db import models
from django.utils import timezone
# from django.contrib.postgres.indexes import GinIndex


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
        return f'{self.name} | {self.category} | {self.brand} | {self.company}'
    
    class Meta:
       indexes = [
           models.Index(fields=['code'], name='product_code_index'),
           models.Index(fields=['company'], name='product_company_index'),
           models.Index(fields=['brand'], name='product_brand_index'),
           models.Index(fields=['category'], name='product_category_index'),
       ] 
       # GinIndex(fields=['name'], name='product_name_trigram_index'), # habilitar en postgrest CREATE EXTENSION IF NOT EXISTS pg_trgm;
       # El índice trigram es especialmente útil cuando los usuarios buscan coincidencias parciales LIKE o ILIKE
    

class Stock(models.Model):
    code = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='Stock', to_field='code', db_column='code', default='999999999')
    stock = models.IntegerField(null=True, blank=True)
    datetime_scraper = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.code} | {self.stock}'
    
    class Meta:
        indexes = [
            models.Index(fields=['code'], name='stock_code_index'),
            models.Index(fields=['datetime_scraper'], name='stock_datetime_scraper_index'),
        ]
    
class Price(models.Model):
    code = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='Price', to_field='code', db_column='code', default='999999999')
    price_usd = models.DecimalField(decimal_places = 2, max_digits=10)
    price_pen =models.DecimalField(decimal_places = 2, max_digits=10)
    discount = models.DecimalField(decimal_places = 2, max_digits=10,null=True, blank=True)
    datetime_scraper = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.code} | {self.price_usd} | {self.price_pen}'
    
    class Meta:
        indexes = [
            models.Index(fields=['code'], name='price_code_index'),
            models.Index(fields=['datetime_scraper'], name='price_datetime_scraper_index'),
        ]