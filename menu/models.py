from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Menu(models.Model):
    """ Model to create menu """
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        """ Order by name """
        ordering = ['name']

    def __str__(self):
        return self.name


class AllergyLabel(models.Model):
    """ Model to create allergy labels """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


MENU_CATEGORIES = (
    ("starter", "Starter"),
    ("main", "Main"),
    ("sides", "Sides"),
    ("salads", "Salads"),
    ("drinks", "Drinks"),
    ("desserts", "Desserts"),
    ("chefs special", "Chef's Special")
)


class MenuItem (models.Model):
    """Models to create menu items"""
    menu = models.ForeignKey(
        Menu, related_name='items', on_delete=models.CASCADE
        )
    title = models.CharField(max_length=50)
    category = models.CharField(
        max_length=50, 
        choices=MENU_CATEGORIES,
        default='starter'
    )
    allergy_labels = models.ManyToManyField(
         AllergyLabel, related_name='menu_items', blank=True)
    description = models.TextField(default="")
    price = models.FloatField(default=0.00)

    class Meta:
        """Order by category, title and allergy"""
        ordering = ['category', 'title']

    def __str__(self):
        return self.title
