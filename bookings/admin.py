from django.contrib import admin
from .models import Table, Booking

# Register your models here.


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "capacity"
        )
    list_filter = (
        "number",
        "capacity"
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date",
        "time",
        "table",
        "party_size"
    )
    list_filter = (
        "date",
        "table"
    )
    search_fields = (
        "name",
        "phone",
        "date"
    )
