from django.urls import path

from . import views

urlpatterns = [
    path('create-appoitnment/', views.create_appointment, name='create_appointment'),
    path('appointments/', views.appointments, name='appointments'),
]
