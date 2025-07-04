from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Menu, CreateMenuItem, AllergyLabels
from django.contrib import messages
from django.urls import reverse_lazy
from menu.forms import MenuForm, CreateMenuItemForm, AllergyLabelsForm
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
class CreateMenuItemsView(UpdateView):
    model = CreateMenuItem
    form_class = CreateMenuItemForm
    template_name = 'menu/createmenu_items.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Items added to the menu successfully')
        return super().form_valid(form)
    

@method_decorator(staff_member_required, name='dispatch')
class CreateAllergyLabelsView(CreateView):
    model = AllergyLabels
    form_class = AllergyLabelsForm
    template_name = ''
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Allergy Labels updated successfully')
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class DeleteMenuItemView(DeleteView):
    model = CreateMenuItem
    # form_class = ManageMenuItemForm
    # template_name = 'menu/manage_menu.html'
    template_name = 'menu/delete_menu_item.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        messages.success(self.request, 'Items deleted successfully')
        return super().form_valid(form)

           
