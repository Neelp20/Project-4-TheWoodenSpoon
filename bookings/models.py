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
    """ Model to create a booking """
    TIME_CHOICES = [
        ('12:00', '12:00 - 13:45'),
        ('14:00', '14:00 - 15:45'),
        ('16:00', '16:00 - 17:45'),
        ('18:00', '18:00 - 19:45'),
        ('20:00', '20:00 - 21:45')
        
    ]
    """Model to create bookings"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="booking")

    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
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
        return f"{self.name} | {self.date} {self.time} | Table {
            self.table.number}"
