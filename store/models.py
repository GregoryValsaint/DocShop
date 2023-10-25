from django.db import models

("Product"
 "- Nom"
 "- Prix"
 "- La quantité en stock"
 "- Description"
 "")

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="product", blank=True, null=True)

    def __str__(self):
        return self.name