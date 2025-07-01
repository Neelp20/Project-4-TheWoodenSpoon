from django.db import models
# from cloudinary.models import CloudinaryField

# Create your models here.
# MENU_CATEGORIES = (
#     ("starter", "Starter"),
#     ("main", "Main"),
#     ("sides", "Sides"),
#     ("drink", "Drink"),
#     ("desert", "Desert")
# )


# class MenuItem (models.Model):
#     """Models to create menu items"""
#     user = models.ForeignKey(User, related_name='the_owner', on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     category = models.CharField(
#         max_length=25, 
#         choices=MENU_CATEGORIES, 
#         default='starter'
#     )
#     description = models.TextField(default="")
#     price = models.FloatField(default=0.00)
#     contains_nuts = models.BooleanField(default=False)
#     vegetarian = models.BooleanField(default=False)
#     vegan = models.BooleanField(default=False)
#     gluten_free = models.BooleanField(default=False)

#     class Meta:
#         """Order by category and name"""
#         ordering = ['category', 'name']

#     def __str__(self):
#         return str(self.name)