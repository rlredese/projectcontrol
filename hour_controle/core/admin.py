from django.contrib import admin
from .models import Project, task_register 

admin.site.register(Project)
admin.site.register(task_register)