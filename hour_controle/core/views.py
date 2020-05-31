from django.shortcuts import render
from .models import task_register

def home(request):

    #all_tasks = task_register.object.all()
    #for task in all_tasks:
        #total_time_task =+ task.time_task

    return render(request,'home.html')

def task_register(request):
    return render(request,'task_register.html')

def project_register(request):
    return render(request,'project_register.html')


