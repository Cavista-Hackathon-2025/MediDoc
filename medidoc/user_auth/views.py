import requests

from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.conf import settings


from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import datetime

from django.shortcuts import redirect, render
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import json
import requests

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


def google_login(request):
    """Initiate the OAuth flow for Google Authentication"""
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CREDENTIALS_FILE,
        scopes=settings.GOOGLE_SCOPES,
        redirect_uri="http://127.0.0.1:8000/google/callback/"
    )

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        prompt="consent",
        include_granted_scopes="true"
    )

    request.session["oauth_state"] = state
    return redirect(authorization_url)


def google_callback(request):
    """Handle Google OAuth callback and fetch user credentials"""
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CREDENTIALS_FILE,
        scopes=settings.GOOGLE_SCOPES,
        redirect_uri="http://127.0.0.1:8000/google/callback/"
    )

    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credentials = flow.credentials

    # Store credentials in session (or save them in the database for persistent access)
    request.session["google_access_token"] = credentials.token
    request.session["google_refresh_token"] = credentials.refresh_token
    request.session["google_token_expiry"] = credentials.expiry.isoformat()

    return redirect("/google/calendar/")  # Redirect to the Google Calendar view

def create_calendar_event(request):
    """Creates a new event in the user's Google Calendar."""
    access_token = request.session.get("google_access_token")

    if not access_token:
        return redirect("google_login")

    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

    event_data = {
        "summary": "New Event from Django",
        "location": "Online",
        "description": "Testing Google Calendar API integration",
        "start": {
            "dateTime": (datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat() + "Z",
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": (datetime.datetime.utcnow() + datetime.timedelta(days=1, hours=1)).isoformat() + "Z",
            "timeZone": "UTC",
        },
    }

    response = requests.post(
        "https://www.googleapis.com/calendar/v3/calendars/primary/events",
        headers=headers,
        json=event_data
    )

    if response.status_code == 200 or response.status_code == 201:
        return render(request, "event_created.html", {"event": response.json()})
    else:
        return render(request, "error.html", {"error": response.json()})

def get_upcoming_events(request):
    creds_data = request.session.get('google_credentials')
    if not creds_data:
        return redirect('/google/auth/')  # Redirect to login if no credentials

    creds = Credentials.from_authorized_user_info(eval(creds_data))
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    
    events = events_result.get('items', [])

    return render(request, 'events.h:tml', {'events': events})

def edit_profile(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            profile = user_form.save()
            profile.save()
    else:
        user_form = RegisterForm(instance=request.user)
        
    return render(request, 'edit_profile.html', {'userform':user_form})


def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user':user})

