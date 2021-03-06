from django import forms

from .views import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('status', 'project','data_reg','short_descriptions','critical_points','description')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('start_date','finish_date','costumers')

class TaskDetailsForm(forms.ModelForm):
    class Meta:
        model = TaskDetails
        fields = ('task_details','task_details_date','task_details_time')