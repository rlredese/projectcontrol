from .models import Task, TaskDetails, Project


def get_total_time():
    total_time = 0
    all_task_time = 0
    id_task = 0
    tasks = Task.objects.all()
    task_entri = TaskDetails.objects
    for task in tasks:
        id_task = task.id
        all_task_details = TaskDetails.objects.filter(pk=id_task)
        for task_details in all_task_details:
            all_task_time += task_details.task_details_time 
    return all_task_time

def get_time_by_project(project_id):
    project_time = 0
    return project_time

def get_all_project():
    all_projects = Project.objects.all()
    return all_projects
    
    
    
