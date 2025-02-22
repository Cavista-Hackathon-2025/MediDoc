from django.db import models

from django.conf import settings

# Create your models here.

class Appointment(models.Model):
    
    STATUS = (
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Cancelled'),
    )
    
    APPOINTMENT_TYPES = (
        ('general','General Checkup'),
        ('dental','Dental Checkup'),
        ('therapy','Therapy Checkup'),
        ('rehabilitation','Rehabilitation Checkup'),
        ('maternity','Maternity Checkup'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider = models.ForeignKey(settings.PROVIDER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=50, choices=APPOINTMENT_TYPES)
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f'{self.user.username} - {self.provider.user.username}, {self.date} {self.time}'
    
    
class Medication(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dosage = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()