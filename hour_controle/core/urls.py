from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('task_register', task_register, name='task_register'),
    path('project_register', project_register, name='project_register'),
    path('task/<int:id>', taskview, name="task-view"),
    path('newtask', newtask, name="newtask"),

]