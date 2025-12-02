from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Patient, Visit
from app.forms import PatientForm, VisitForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# Create your views here.

    
# create a custom login
class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('patients')
        return super().get(self.request, *args, **kwargs)
    
# display list of patients that belong to the user
class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patient_list.html'
    context_object_name = 'patients'
    paginate_by = 10

    # access only the patients that belong to the user
    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Patient.objects.filter(doctor=self.request.user)
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query) 
            ) 
        return queryset


# display detail view of patients that belong to the user
class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient_details'

    # access only the patients that belong to the user
    def get_queryset(self):
        return Patient.objects.filter(doctor=self.request.user)
    
    # adding visit details related to the person selected and added above
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        visits = Visit.objects.filter(person=self.object)

        if query:
            visits = visits.filter(
                Q(date__icontains=query) |
                Q(notes__icontains=query)
            )
    
        context['visits'] = visits
        return context
    
    # make sure the patinet details are not opened with the direct url by another user
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.doctor != self.request.user:
            raise PermissionDenied()
        return obj
    
# display all visits
class VisitListView(LoginRequiredMixin, ListView):
    model = Visit
    template_name = 'visit_list.html'
    context_object_name = 'visits'
    paginate_by = 10

    # access only the patients that belong to the user
    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Visit.objects.filter(doctor=self.request.user)
        if query:
            queryset = queryset.filter(
                Q(person__first_name__icontains=query) | Q(person__last_name__icontains=query) |
                Q(date__icontains=query) | Q(notes__icontains=query)
            ) 
        return queryset
    
    

# display visit details by accessing visit's own fields and accessing person through pk
class VisitDetailView(LoginRequiredMixin, DetailView):
    model = Visit
    template_name = 'visit_detail.html'
    context_object_name = 'visit_details'
    
    # make sure the visit details are not opened with the direct url by another user
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.doctor != self.request.user:
            raise PermissionDenied()
        return obj

# add patients to the system
class AddPatientView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'add_patient.html'
    success_url = reverse_lazy('patients')

    # make sure that added patients' doctor is assigned by defualt (user)
    # display the message after successfully adding the patient
    def form_valid(self, form):
        form.instance.doctor = self.request.user
        messages.success(self.request, "Patient added successfully.")
        return super().form_valid(form)

    

# add visits to the systems
class AddVisitView(LoginRequiredMixin, CreateView):
    model = Visit
    form_class = VisitForm
    template_name = 'add_visit.html'

    # redirect to the visit history of the patient
    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.person.pk})
    
    # to autofill patient if visited from visit history
    def get_initial(self):
        initial = super().get_initial()
        person_pk = self.kwargs.get('pk')
        if person_pk:
            initial['person'] = person_pk
        return initial
    
    # make sure that added patients' doctor is assigned by defualt (user)
    def form_valid(self, form):
        form.instance.doctor = self.request.user
        messages.success(self.request, "Visit added successfully.")
        return super().form_valid(form)
    
    # make sure the patients belong to the user
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['person'].queryset = Patient.objects.filter(doctor=self.request.user)
        return form
    
# update the existing patient info
class UpdatePatientView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'update_patient.html'
    success_url = reverse_lazy('patients')

    # only allow user to update their patients (protect users from accessing other patients via url)
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.doctor != self.request.user:
            raise PermissionDenied()
        return obj
    
    # display the success message
    def form_valid(self, form):
        messages.success(self.request, "Patient updated successfully.")
        return super().form_valid(form)

# update the existing visit info
class UpdateVisitView(LoginRequiredMixin, UpdateView):
    model = Visit
    form_class = VisitForm
    template_name = 'update_visit.html'
    
    # allow the user to only update the visit of the patient they own
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.doctor != self.request.user:
            raise PermissionDenied()
        return obj
    
    # after updating visits go to the visit history page
    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.person.pk})
    
    # display the success message
    def form_valid(self, form):
        messages.success(self.request, "Visit updated successfully.")
        return super().form_valid(form)
    
# delete the patient
class DeletePatientView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Patient
    template_name = 'delete_patient.html'
    success_url = reverse_lazy('patients')
    success_message = "Patient deleted successfully"

    # allow the user to delete only the patients they own
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.doctor != self.request.user:
            raise PermissionDenied()
        return obj

# delete the visit
class DeleteVisitView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Visit
    template_name = 'delete_visit.html'
    success_message = "Visit deleted successfully"

    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.person.pk})
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.doctor != self.request.user:
            raise PermissionDenied()
        return obj
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Visit deleted successfully.")
        return super().delete(request, *args, **kwargs)
        

    
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_403(request, exception):
    return render(request, '403.html', status=403)

def custom_400(request, exception):
    return render(request, '400.html', status=400)


