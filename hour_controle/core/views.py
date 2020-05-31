from django.shortcuts import render
from .models import task_register

def home(request):
    
    return render(request,'home.html')

def task_register(request):
    return render(request,'task_register.html')

def project_register(request):
    return render(request,'project_register.html')


