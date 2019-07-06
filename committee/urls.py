from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_comt,name='create-comt'),
    path('list/', views.comt_list,name='comt-list'),
    path('edit/<comt_id>', views.edit_comt,name='edit-comt'),
    path('delete/<comt_id>',views.delete_comt,name='delete-comt')
]
