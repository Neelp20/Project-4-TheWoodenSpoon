from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.db.models import Q
from .models import Booking
from .forms import BookingForm


# User Views
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "bookings/manage_bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user,
            date__gte=date.today()
        ).order_by("date", "time")


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/bookings.html"
    success_url = reverse_lazy("manage-bookings")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.table = form.cleaned_data["table_obj"]
        messages.success(self.request, "Booking created successfully.")
        return super().form_valid(form)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/edit_booking.html"
    success_url = reverse_lazy("manage-bookings")

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.table = form.cleaned_data["table_obj"]
        messages.success(self.request, "Booking updated successfully.")
        return super().form_valid(form)


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = "bookings/confirm_delete_booking.html"
    success_url = reverse_lazy("manage-bookings")

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Booking cancelled successfully.")
        return super().delete(request, *args, **kwargs)


class PastBookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "bookings/past_bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user,
            date__lt=date.today()
        ).order_by("-date", "-time")


# Admin views
class AdminBookingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Booking
    template_name = "bookings/admin_manage_bookings.html"
    context_object_name = "bookings"

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        queryset = Booking.objects.filter(
            date__gte=date.today()
        ).order_by("date", "time")
    
        search_query = self.request.GET.get("q")
        date_filter = self.request.GET.get("date")

        if search_query:
            queryset = queryset.filter(
               Q(name__icontains=search_query) |
               Q(email__icontains=search_query)
            )

        if date_filter:
            queryset = queryset.filter(date=date_filter)

        return queryset


