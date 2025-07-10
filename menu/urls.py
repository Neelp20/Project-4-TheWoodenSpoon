from django.urls import path 
from . import views

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('create_menu/', views.CreateMenuView.as_view(), name='create_menu'),
    path('create_menu_item/', views.CreateMenuItemsView.as_view(), name='create_menu_item'),
    path('create_allergy_label/', views.CreateAllergyLabelsView.as_view(), name='create_allergy_label'),
    path('deletemenuitem/<int:pk>/', views.DeleteMenuItemView.as_view(), name='deletemenuitems'),
    path('editmenu/<int:pk>/', views.EditMenuItemView.as_view(), name='editmenu'),
    path('manage/', views.ManageMenuView.as_view(), name='managemenus'),
]
