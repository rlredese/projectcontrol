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