from django import forms
from .models import Menu, MenuItem, AllergyLabel


class MenuForm(forms.ModelForm):
    """ Form to create menu"""
    class Meta:
        model = Menu
        fields = [
            'name',
            'active',

            ]


class MenuItemForm(forms.ModelForm):
    """
    Form to create menu items with checkboxes
    """
    class Meta:
        model = MenuItem
        fields = [
            'menu',
            'title',
            'category',
            'description',
            'price',
            'allergy_labels'

            ]
        widgets = {
            'allergy_labels': forms.CheckboxSelectMultiple
        }


class AllergyLabelsForm(forms.ModelForm):
    """
    Form to craete allergy labels
    """
    class Meta:
        model = AllergyLabel
        fields = [
            'name'
        ]
