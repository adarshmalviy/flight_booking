from django import forms
from .models import Flight
from django.forms.widgets import DateTimeInput

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'departure_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
