from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    # add other paths as needed
    path('create_menu/', views.CreateMenuView.as_view(),
         name='create_menu'),
    path('create_menu_item/', views.CreateMenuItemsView.as_view(),
         name='create_menu_item'),
    path('createmenuitem/', views.CreateAllergyLabelsView.as_view(),
         name='createmenuitems'),
    path('deletemenuitem/', views.DeleteMenuItemView.as_view(),
         name='deletemenuitems'),
    path('editmenu/', views.EditMenuItemView.as_view(),
         name='editmenu'),
    path('manage/', views.ManageMenuView.as_view(),
         name='managemenus')


]