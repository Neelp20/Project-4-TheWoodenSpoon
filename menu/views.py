from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Menu, MenuItem, AllergyLabel, MENU_CATEGORIES
from django.contrib import messages
from django.urls import reverse_lazy
from menu.forms import MenuForm, MenuItemForm, AllergyLabelsForm
from django.shortcuts import render

# Create your views here.


def menu_view(request):
    """ Create menu view to create a menu if user is staff """
    items = MenuItem.objects.prefetch_related('allergy_labels')
    grouped_menu = {
        label: [item for item in items if item.category == key]
        for key, label in MENU_CATEGORIES
    }
    return render(request, 'menu/menu.html', {'grouped_menu': grouped_menu})


@method_decorator(staff_member_required, name='dispatch')
class CreateMenuView(CreateView):
    """ Create menu view to create a menu if user is staff """
    model = Menu
    form_class = MenuForm
    template_name = 'menu/create_menu.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Menu created successfully')
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class CreateMenuItemsView(CreateView):
    """ Create menu items view to create a menu items if user is staff """
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/create_menu_items.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.allergy_labels.set(form.cleaned_data['allergy_labels'])
        messages.success(self.request, 'Item added to the menu successfully')
        return response


@method_decorator(staff_member_required, name='dispatch')
class CreateAllergyLabelsView(CreateView):
    """ Create allergy label view to create allergy label if user is staff """
    model = AllergyLabel
    form_class = AllergyLabelsForm
    template_name = 'menu/create_allergy_label.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Allergy Labels updated successfully')
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class DeleteMenuItemView(DeleteView):
    """ Delete menu item view to delete a menu item if user is staff """
    model = MenuItem
    template_name = 'menu/delete_menu_item.html'
    success_url = reverse_lazy('managemenus')

    def form_valid(self, form):
        messages.success(self.request, 'Menu item deleted successfully')
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class EditMenuItemView(UpdateView):
    """ Edit menu item view to edit a menu item if user is staff """
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/edit_menu.html'
    success_url = reverse_lazy('managemenus')

    def form_valid(self, form):
        messages.success(self.request, 'Menu item updated successfully')
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class ManageMenuView(ListView):
    """Manage menu item view to manage a menu item if user is staff"""
    model = MenuItem
    template_name = 'menu/manage_menu.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return MenuItem.objects.select_related(
            'menu'
            ).prefetch_related(
                'allergy_labels'
                ).order_by(
                    'category', 'title')
