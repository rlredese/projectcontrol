from django.shortcuts import render, get_object_or_404
from .models import Task

def home(request):
  
    
    return render(request,'home.html')

def task_register(request):
    all_tasks = Task.objects.all()
    return render(request,'task_register.html',{'all_tasks':all_tasks})

def taskview(request,id):
    task = get_object_or_404(Task,pk=id)
    return render(request,'taskview.html',{'task':task})

def project_register(request):
   
    return render(request,'project_register.html')


