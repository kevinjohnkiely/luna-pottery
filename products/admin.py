from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_code',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('product_code',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'front_end_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
