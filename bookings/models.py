from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Table(models.Model):
    """Model to create Tables"""
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} (Seats: {self.capacity})"
 

class Booking(models.Model):
    """Model to create bookings"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="booking")

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        unique_together will ensure to avoid double-bookings.
        Order by date and then time
        """
        unique_together = ("table", "date", "time")
        ordering = ("date", "time")

    def __str__(self):
        return f"{self.name} | {self.date} {self.time} | Table {self.table.number}"
