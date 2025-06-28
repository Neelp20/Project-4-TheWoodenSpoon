from django.db import models
from django.contrib.auth.models import User


# Choice fields
MENU_CATEGORIES = (
    ("starter", "Starter"),
    ("main", "Main"),
    ("desert", "Desert"),
    ("drink", "Drink"),
    ("side", "Side")

)

# Create your models here.


class MenuItem(models.Model):
    """ Model to create menu items"""
    name = models.CharField(max_length=50)
    category = models.CharField(
        max_length=25, choices=MENU_CATEGORIES, default='starter'
    )
    description = models.TextField(default="")
    price = models.FloatField(default=0.00)
    contains_nuts = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    
    class Meta:
        """Order by type and name"""
        ordering = ['category', 'name']

    def __str__(self):
        return str(self.name)

