from django.db import models

class Task(models.Model):
    STATUS = (
        ('wg','Aguardando'),
        ('eg','Em Execução'),
        ('dn','Concluído')
    )
    status = models.CharField(max_length=2,choices=STATUS,blank=True,default="Aguardando")
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name='project')
    data_reg = models.DateTimeField()
    time_task = models.IntegerField(blank=True,null=True)
    short_descriptions = models.CharField(max_length=50,null=True)
    critical_points = models.CharField(max_length=300,null=True,blank=True)
    description = models.TextField()
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.short_descriptions

class TaskDetails(models.Model):
    id_task = models.ForeignKey("Task", on_delete=models.CASCADE, related_name='task')
    task_details = models.CharField(max_length=500)
    task_details_date = models.DateTimeField(null=True)
    task_details_time = models.IntegerField(blank=True,null=True)
    detail = str(id_task)
    def __str__(self):
        return self.detail
    


class Project(models.Model):
    start_date = models.DateField(null=False)
    finish_date = models.DateField(null=True)
    costumers = models.CharField(max_length=50)
    
    def __str__(self):
        return self.costumers


    



