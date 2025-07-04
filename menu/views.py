from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Menu, MenuItem, AllergyLabel
from django.contrib import messages
from django.urls import reverse_lazy
from menu.forms import MenuForm, MenuItemForm, AllergyLabelsForm
from django.shortcuts import render

# Create your views here.


def menu_view(request):
    return render(request, 'menu/menu.html')


@method_decorator(staff_member_required, name='dispatch')
class CreateMenuView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/create_menu.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Menu created successfully')
        return super().form_valid(form)
    

@method_decorator(staff_member_required, name='dispatch')
class CreateMenuItemsView(CreateView):
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
    model = AllergyLabel
    form_class = AllergyLabelsForm
    template_name = 'menu/createmenu_items.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Allergy Labels updated successfully')
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class DeleteMenuItemView(DeleteView):
    model = MenuItem
    # form_class = ManageMenuItemForm
    # template_name = 'menu/manage_menu.html'
    template_name = 'menu/delete_menu_item.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Items deleted successfully')
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class EditMenuItemView(UpdateView):
    model = Menu
    template_name = 'menu/edit_menu.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Edited successfully')
        return super().form_valid(form)
    

@method_decorator(staff_member_required, name='dispatch')
class ManageMenuView(ListView):
    """Manage menu view"""
    model = MenuItem
    template_name = 'menu/manage_menu.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return MenuItem.objects.select_related(
            'menu', 'category').prefetch_related(
                'allergy_labels').order_by(
                    'menu', 'category', 'title')
