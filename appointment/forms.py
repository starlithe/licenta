from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ['name', 'phone_number', 'day', 'appointment', 'frizer', 'pachet']
        
        # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)

        # self.fields['name'].widget.attrs.update(
        #     {'class': 'form-select'})

        # self.fields['phone_number'].widget.attrs.update(
        #     {'class': 'form-select'})

        # self.fields['day'].widget.attrs.update(
        #     {'class': 'form-select'})

        # self.fields['appointment'].widget.attrs.update(
        #     {'class': 'form-select'})

        # self.fields['frizer'].widget.attrs.update(
        #     {'class': 'form-select'})

        # self.fields['pachet'].widget.attrs.update(
        #     {'class': 'form-select'})