from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('add-category', views.add_category, name='add_category'),
    path('<str:slug>', views.job_detial, name='job_detial'),
]
