from django import forms

from .models import CustomUser, Provider, Patient
from datetime import datetime , timedelta

class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=(forms.PasswordInput))
    confirm_password = forms.CharField(widget=(forms.PasswordInput))
    
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'role', 'profile_image']
        widgets = {
            'email':forms.EmailInput({'type':'email'}),
        }
        
        
class ProviderForm(forms.ModelForm):
    
    class Meta:
        model = Provider
        fields = ['speciality', 'provider_date_of_birth']
        widgets = {
            'provider_date_of_birth':forms.DateInput({'type':'date'})
        }
        
class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ['date_of_birth']
        widgets = {
            'date_of_birth':forms.DateInput({'type':'date', 'placeholder':'YYYY-MM-DD'})
        }
   
