from django.db import models
from django.contrib.auth.models import User

RATINGS = ((None, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=200)
    front_end_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_front_end_name(self):
        return self.front_end_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_code = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(default='Product Description')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=0.0)
    in_stock_amount = models.IntegerField(null=True, blank=True, default=50)
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products_rating")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_rating")
    rating = models.IntegerField(choices=RATINGS, null=True, blank=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products_review")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_review")
    review_text = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlist_product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist_user")