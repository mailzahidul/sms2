"""sms2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('administration/', views.staff_registration, name='staff-registration'),
    path('list/', views.staff_list, name='staff-list'),
    path('edit/<staff_id>', views.edit_staff, name='edit-staff'),
    path('delete/<staff_id>', views.delete_staff, name='delete-staff'),
    path('details/<staff_id>', views.staff_details, name='staff-details'),
]

