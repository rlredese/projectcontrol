from django.urls import path
from core.views import home, task_register, project_register,taskview

urlpatterns = [
    path('', home, name='home'),
    path('task_register', task_register, name='task_register'),
    path('project_register', project_register, name='project_register'),
    path('task/<int:id>', taskview, name="task-view"),

]