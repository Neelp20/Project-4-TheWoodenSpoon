from django import forms
from .models import Menu, MenuItem, AllergyLabel


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'name',
            'active',

            ]


class MenuItemForm(forms.ModelForm):
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
    class Meta:
        model = AllergyLabel
        fields = [
            'name'
        ]