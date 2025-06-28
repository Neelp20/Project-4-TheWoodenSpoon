from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Lists field for display menu items"""
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)

# Register your models here.