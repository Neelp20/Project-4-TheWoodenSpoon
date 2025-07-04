from django import forms
from .models import Menu, CreateMenuItem, AllergyLabels


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'name',
            'active',

            ]


class CreateMenuItemForm(forms.ModelForm):
    class Meta:
        model = CreateMenuItem
        fields = [
            'menu',
            'title',
            'category',
            'description',
            'price'
            
            ]
        

class AllergyLabelsForm(forms.ModelForm):
    class Meta:
        model = AllergyLabels
        fields = {
            'allergy_labels'
        }