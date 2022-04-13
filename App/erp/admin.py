from unicodedata import category
from django.contrib import admin
from App.erp.models import Category, Product, Client, Sale, DetSale

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Sale)
admin.site.register(DetSale)
