from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
       
        fields = ['firstname', 'lastname', 'age', 'contact', 'address', 'street', 'city', 'doctor', 'pincode']