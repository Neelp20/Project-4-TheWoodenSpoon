from django.db import models
from django.contrib.auth.models import User
# from django_summernote.admin import SummernoteModelAdmin
# from cloudinary.models import CloudinaryField

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        """ Order by name """
        ordering = ['name']

    def __str__(self):
        return str(self.name)


ALLERGY_LABELS = (
    ("contains dairy", "Contains Dairy"),
    ("contains nuts", "Contains Nuts"),
    ("vegetarian", "Vegetarian"),
    ("vegan", "Vegan"),
    ("gluten free", "Gluten Free")
    
)


class AllergyLabels(models.Model):
    name = models.CharField(max_length=50, unique=True)
    allergy_labels = models.CharField(
        max_length=50,
        choices=ALLERGY_LABELS,
        default=None
    )
    contains_dairy = models.BooleanField(default=False)
    contains_nuts = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    
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


class CreateMenuItem (models.Model):
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

    description = models.TextField(default="")
    price = models.FloatField(default=0.00)

    class Meta:
        """Order by category, title and allergy"""
        ordering = ['category', 'title']

    def __str__(self):
        return str(self.name)
