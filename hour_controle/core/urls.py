from django.urls import path
from core.views import home, task_register, project_register

urlpatterns = [
    path('', home, name='home'),
    path('task_register', task_register, name='task_register'),
    path('project_register', project_register, name='project_register'),
]