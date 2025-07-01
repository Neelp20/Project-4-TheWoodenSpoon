from django.contrib import admin
from .models import MenuItem

# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Lists field to display menu items"""
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)