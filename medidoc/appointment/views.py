import os
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from datetime import datetime

from .forms import AppointmentForm, PrescriptionForm

from .models import Medication, Appointment

# Create your views here.

@login_required
def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            time = form.cleaned_data.get('time')
            print(time, date)
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'appointmentform':form})

@login_required
def appointments(request):
    user = request.user
    now = timezone.now()
    upcoming_appointments = Appointment.objects.filter(user=request.user, date__gte=now.date()).order_by('date', 'time')
    
    past_appointment = Appointment.objects.filter(user=request.user, date__lt=now.date()).order_by('date', 'time')
    
    appointments = Appointment.objects.filter(user=request.user)
    
    cancelled_appointments = Appointment.objects.filter(status='cancelled')
    context = {
        'appointments':appointments,
        'upcoming':upcoming_appointments,
        'user':user,
        'cancelled':cancelled_appointments,
        'past':past_appointment
    }
    
    return render(request, 'appointments.html', context=context)

