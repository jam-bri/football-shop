from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=200)       # item name
    price = models.PositiveIntegerField()         # item price
    description = models.TextField()               # item description
    thumbnail = models.URLField()                  # item image URL
    category = models.CharField(max_length=100)    # item category
    is_featured = models.BooleanField()            # featured status
    stock = models.PositiveIntegerField()                  # item stock quantity positive integer
    rating = models.FloatField()                   # item rating
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    