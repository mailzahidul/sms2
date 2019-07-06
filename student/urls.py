from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_student, name='create-student'),
    path('list/', views.student_list, name='student-list'),
    path('edit/<student_id>', views.student_edit, name='student-edit'),
    path('delete/<student_id>', views.student_delete, name='student-delete'),
    path('detail/<student_id>', views.student_detail, name='student-detail'),
    path('search/', views.student_search, name='student-search'),
    path('register/', views.register_student, name='student-register'),
    path('att-count/', views.attendance_count, name='attendance-count'),
]
