from django.shortcuts import render
from .models import task_register

def home(request):
    all_registers = task_register.objects.all()
    return render(request,'home.html',{'all_registers':all_registers})


