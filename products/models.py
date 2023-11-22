from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Category(models.TextChoices):
    COMPUTERS = 'Computers'
    KIDS = "Kids"
    FOOD = "Food"
    HOME = "Home"



class Product(models.Model):
    name = models.CharField(max_length=200, default="", blank=False)
    description = models.TextField(max_length=200, default="", blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    brand = models.CharField(max_length=40, blank=True)
    category = models.CharField(max_length=40, choices=Category.choices)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    comment = models.TextField(max_length=200, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.product:
            return f"review for product {self.product.name}"
        else:
            return "review with no associated product"
