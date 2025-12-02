from django.urls import path
from .views import (PatientListView, PatientDetailView, 
                    VisitDetailView, AddPatientView, 
                    AddVisitView, UpdatePatientView, 
                    UpdateVisitView, DeletePatientView,
                    DeleteVisitView, VisitListView,
                    CustomLoginView)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('patients/', PatientListView.as_view(), name='patients'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('visits/', VisitListView.as_view(), name='visits'),
    path('visits/<int:pk>/', VisitDetailView.as_view(), name='visit_details'),
    path('add_patient', AddPatientView.as_view(), name='add_patient'),
    path('add_visit/<int:pk>/', AddVisitView.as_view(), name='add_visit'),
    path('add_visit', AddVisitView.as_view(), name='add_visit'),
    path('update_patient/<int:pk>/', UpdatePatientView.as_view(), name ='update_patient'),
    path('update_visit/<int:pk>/', UpdateVisitView.as_view(), name='update_visit'),
    path('delete_patient/<int:pk>/', DeletePatientView.as_view(), name='delete_patient'),
    path('delete_visit/<int:pk>/', DeleteVisitView.as_view(), name='delete_visit'),
]
