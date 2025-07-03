from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings_view, name='bookings'),
    # add other paths as needed
]