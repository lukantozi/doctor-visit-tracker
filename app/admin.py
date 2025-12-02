from django.contrib import admin
from app.models import Patient, Visit

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    search_fields = ['first_name', 'last_name']

admin.site.register(Patient, PatientAdmin)

class VisitAdmin(admin.ModelAdmin):
    list_display = ('person', 'doctor', 'date')
    search_fields = ['person__first_name', 'person__last_name']
    list_filter = ('doctor', 'date')

admin.site.register(Visit, VisitAdmin)