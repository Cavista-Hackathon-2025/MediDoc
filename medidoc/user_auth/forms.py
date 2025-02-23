from django import forms

from .models import CustomUser, Provider, Patient
from datetime import datetime , timedelta

class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=(forms.PasswordInput(attrs={'type':'password', 'class':'form-control'})))
    confirm_password = forms.CharField(widget=(forms.PasswordInput(attrs={'type':'password', 'class':'form-control'})))
    
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'role', 'profile_image']
        widgets = {
            'email':forms.EmailInput({'type':'email', 'class':'form-control'}),
            'username':forms.TextInput({'type':'text', 'class':'form-control'}),
            'first_name':forms.TextInput({'type':'text', 'class':'form-control'}),
            'last_name':forms.TextInput({'type':'text', 'class':'form-control'}),
        }
        
        
class ProviderForm(forms.ModelForm):
    
    class Meta:
        model = Provider
        fields = ['speciality', 'provider_date_of_birth']
        widgets = {
            'provider_date_of_birth':forms.DateInput({'type':'date', 'class':'form-control'}),
            'speciality':forms.TextInput({'type':'text', 'class':'form-control'})
        }
        
        
class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ['date_of_birth']
        widgets = {
            'date_of_birth':forms.DateInput({'type':'date', 'class':'form-control', 'placeholder':'YYYY-MM-DD'})
        }
   
