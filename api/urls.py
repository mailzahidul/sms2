from django.urls import path
from . import views

urlpatterns = [
    path('attendance/<std_cls>/<std_roll>/', views.StudentAttendance.as_view(), name='create-student'),
    path('result/', views.ResultViews.as_view(), name='create-student'),
]
