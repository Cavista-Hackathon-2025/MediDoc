from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
    
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female'),
    )
    
    ROLE_CHOICES = (
        ('patient','Patient'),
        ('provider','Provider'),
    )
    
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    profile_image = models.ImageField(upload_to='profile_pics/', default='profile_pics/8.jpg', blank=True, null=True)
    
    groups = models.ManyToManyField(Group, related_name='Customuser_set', blank=True)
    
    user_permissions = models.ManyToManyField(Permission, related_name='CustomUser_permissions_set', blank=True)
    
    def __str__(self):
        return self.username
    
class Provider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=20, blank=True, null=True)
    provider_date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)