from datetime import datetime, timedelta
from django.core.exceptions import ValidationError  # Custom validation error
from django import forms  # To create a django form
from .models import Table, Booking


class BookingForm(forms.ModelForm):
    """Form to create/edit a booking"""
    
    class Meta:
        model = Booking
        fields = [
            "name",
            "email",
            "phone",
            "date",
            "time",
            "party_size",
            "message"
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.Select(choices=Booking.TIME_CHOICES),
            'message': forms.Textarea(
                attrs={'placeholder': 'Any message please let us know'}
                ),
        }

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop("user", None)
            super().__init__(*args, **kwargs)
            today = datetime.now().date()
            self.fields['date'].widget.attrs['min'] = today.strftime(
                '%Y-%m-%d'
                )

        def clean(self):
            cleaned_data = super().clean()
            date = cleaned_data.get("date")
            time = cleaned_data.get("time")
            party_size = cleaned_data.get("party_size")

            if not date or not time or not party_size:
                raise ValidationError("Please fill in all required fields.")

            # if date and time:
                # Combine date and time into a datetime object
            booking_datetime = datetime.combine(date, time)
            now_plus_24h = datetime.now() + timedelta(hours=24)

            if booking_datetime < now_plus_24h:
                raise ValidationError(
                    "Bookings must be made at least 24 hours in advance."
                    )

        # Find tables that are large enough
            candidate_tables = Table.objects.filter(
               capacity__gte=party_size
            )

        # Exclude tables already booked at that slot
            candidate_tables = candidate_tables.exclude(
               booking__date=date,
               booking__time=time,
            )

            if not candidate_tables.exists():
                raise ValidationError(
                 "No available tables for this party size and timeslot."
                 "Please call us to enquire"
                )

        # attach first available table so view can save it
            cleaned_data["table_obj"] = candidate_tables.first()
            return cleaned_data
        
