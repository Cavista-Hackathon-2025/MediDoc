# Generated by Django 5.1.3 on 2025-02-22 13:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '0002_customuser_profile_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('type', models.CharField(choices=[('general', 'General Checkup'), ('dental', 'Dental Checkup'), ('therapy', 'Therapy Checkup'), ('rehabilitation', 'Rehabilitation Checkup'), ('maternity', 'Maternity Checkup')], max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], max_length=20)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_auth.provider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dosage', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment')),
            ],
        ),
    ]
