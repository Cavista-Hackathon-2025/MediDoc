from django import forms
from django.conf import settings
from django.apps import apps
from django_select2.forms import Select2Widget
from datetime import datetime
from .models import Appointment, Medication  # Ensure you import your Appointment model

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ['provider', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'provider': Select2Widget
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # ✅ Dynamically resolve the model from settings
        ProviderModel = apps.get_model(settings.PROVIDER_MODEL)
        self.fields['provider'].queryset = ProviderModel.objects.all()

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.now().date():
            raise forms.ValidationError('Date cannot be in the past')
        return date
    
    def clean_time(self):
        time = self.cleaned_data['time']
        if time < datetime.now().time():
            raise forms.ValidationError('Time cannot be in the past')
        return time


class PrescriptionForm(forms.ModelForm):
    
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'start_date', 'end_date']
        widgets = {
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'}),
        }