from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'list.html', {'appointments':appointments})