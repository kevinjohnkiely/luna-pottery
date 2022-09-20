from django.contrib import admin
from .models import Product, Category, Rating, Review, Wishlist


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_code',
        'name',
        'category',
        'price',
        'in_stock_amount',
        'rating',
        'image',
    )

    ordering = ('product_code',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'front_end_name',
        'name',
    )


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating'
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'review_text',
        'created_at'
    )


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
