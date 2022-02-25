from django.contrib import admin

from .models import Product, ProductAmount, Recipe


admin.site.register(Product)
admin.site.register(ProductAmount)
admin.site.register(Recipe)
