from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# create fields for patients
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    date_of_birth = models.DateField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# create fields for visits
class Visit(models.Model):
    person = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True)

    # when called, represent these
    def __str__(self):
        return f"Visit: {self.person} with Dr. {self.doctor.username} on {self.date} "