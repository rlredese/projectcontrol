# Generated by Django 3.0.6 on 2020-06-04 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200531_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_details', models.CharField(max_length=500)),
                ('id_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='core.Task')),
            ],
        ),
    ]