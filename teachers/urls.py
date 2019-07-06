from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.create_teacher,name='create-teacher'),
    path('list/',views.teacher_list,name='teacher-list'),
    path('edit/<teacher_id>',views.teacher_edit,name='teacher-edit'),
    path('delete/<teacher_id>',views.teacher_delete,name='teacher-delete')
]
