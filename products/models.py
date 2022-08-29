from django.db import models


class Category(models.Model):
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
    name = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name