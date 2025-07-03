from django.shortcuts import render

# Create your views here.


def bookings_view(request):
    return render(request, 'bookings/bookings.html')