from django.shortcuts import render, get_object_or_404
from .models import Task, TaskDetails


def home(request):
    all_tasks = Task.objects.all()
    total_time = 0
    for task in all_tasks:
        if task.time_task == 'NoneTipe':
            total_time += task.time_task
    context = {'total_time': total_time}    
    return render(request,'home.html',context)

def task_register(request):
    all_tasks = Task.objects.all()
    return render(request,'task_register.html',{'all_tasks':all_tasks})

def newtask(request):
    return render(request,'newtask.html')

def taskview(request,id):
    task = get_object_or_404(Task,pk=id)
    task_entri = TaskDetails.objects.all()
    context = {'task':task,'task_entri':task_entri}
    return render(request,'taskview.html',context)

def project_register(request):
   
    return render(request,'project_register.html')


