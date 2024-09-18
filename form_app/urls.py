from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_application_view, name='application_form'),
    path('success/', views.success_view, name='success'),
    path('all/', views.application_form_list_view, name='form_list'),
    path('all-clients/', views.all_clients_view, name='all_clients'),
    path('add-client/', views.add_client_view, name='add_client'),  # URL for adding a new client
]
