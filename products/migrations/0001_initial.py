# Generated by Django 5.1 on 2024-08-20 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.CharField(blank=True, max_length=300, null=True)),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_pen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_status', models.BooleanField(blank=True, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('datetime_scraper', models.DateTimeField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='products.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='products.category')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='products.company')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_pen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('datetime_scraper', models.DateTimeField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Price', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('datetime_scraper', models.DateTimeField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Stock', to='products.product')),
            ],
        ),
    ]
