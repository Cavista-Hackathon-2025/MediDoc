from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


from .forms import RegisterForm, PatientForm, ProviderForm

# Create your views here.

@login_required
def home(request):
    user = request.user
    
    return render(request, 'index.html', {'user':user})

def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST, request.FILES)
        providerform = ProviderForm(request.POST)
        patientform = PatientForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            if user.role == 'provider':
                provider = providerform.save(commit=False)
                provider.user = user
                provider.save()
            
            if user.role == 'patient':
                patient = patientform.save(commit=False)
                patient.user = user
                patient.save()
                
            login(request, user)
            return redirect('home')
        
    else:
        user_form = RegisterForm()
        providerform = ProviderForm()
        patientform = PatientForm()
        
    context = {
        'registerform':user_form,
        'patientform':patientform,
        'providerform':providerform
    }
    
    return render(request, 'register.html', context=context)

def user_login(request):
    if request.method == "POST":
        loginform = AuthenticationForm(data=request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        loginform = AuthenticationForm()
        
    return render(request, 'login.html', {'loginform':loginform})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def index(request):
    return render(request, 'landingpage.html')