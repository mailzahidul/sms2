from django.urls import path
from . import views

urlpatterns = [
    path('employee/create/', views.create_employee, name='employee-create')
]
