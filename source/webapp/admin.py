from django.contrib import admin
from webapp.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'stock', 'category']
    list_filter = ['title']
    exclude = []

admin.site.register(Product, ProductAdmin)