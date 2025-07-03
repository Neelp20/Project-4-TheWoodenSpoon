from django.shortcuts import render
# from django.views.generic import CreateView
# from .models import MenuItem

# Create your views here.


def menu_view(request):
    return render(request, 'menu/menu.html')

# class AddMenu(CreateView):
#     """Add menu view"""
#     template_name = 'menu/add_menu.html'
#     model = MenuItem
#     success_url = '/menu/'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(AddMenu, self).form_valid(form)
           
