from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, TaskDetails
from .core_function import *
from .forms import TaskForm, ProjectForm


def home(request):
    total_time = get_total_time()
    all_project = get_all_project()
    context = {'total_time': total_time , 'all_project': all_project}    
    return render(request,'home.html',context)

def task_register(request):
    all_tasks = Task.objects.all().order_by('update_at')
    return render(request,'task_register.html',{'all_tasks':all_tasks})

def newtask(request):
    task = Task
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if (form.is_valid()):
            task = form.save(commit='false')
            task.save()
            return redirect('task_register')        
    else:
        form = TaskForm()
        return render(request,'newtask.html',{'form':form})

def taskview(request,id):
    tasks = Task.objects.filter(id=id)
    task_entri = TaskDetails.objects
    for task in tasks:
        task_entri = TaskDetails.objects.filter(id_task_id=id)
        context = {'task':task,'task_entri':task_entri}
    return render(request,'taskview.html',context)

def task_edit(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if (request.method =="POST"):
        form = TaskForm(request.POST)
        if (form.is_valid()):
            task = form.save(commit='false')
            task.save()
            return redirect('/') 
        else:

            return render(request,'task_edit.html',{'form':form, 'task':task})

    else:
        return render(request,'task_edit.html',{'form':form, 'task':task})

def project_register(request):
    project = Project
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if (form.is_valid()):
            project = form.save(commit='false')
            project.save()
            return redirect('/')        
    else:
        form = ProjectForm()
        return render(request,'project_register.html',{'form':form})
   
    return render(request,'project_register.html')

def helpdesk(request):
    return render(request,'helpdesk.html')


