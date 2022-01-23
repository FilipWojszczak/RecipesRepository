from django.contrib import admin

from .models import Product, Recipe


admin.site.register(Product)
admin.site.register(Recipe)
