from django.forms import ModelForm
from app.models import Patient, Visit
from django import forms

# create PatientForms based on the Patient model created in models.py
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        exclude = ['doctor']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name.lower() in ['test', 'abc', '123']:
            raise forms.ValidationError('Invalid name, please use a real name.')
        return first_name

# create VisiForm based on the Visit model craeted in models.py
class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ["person", "date", "notes"]