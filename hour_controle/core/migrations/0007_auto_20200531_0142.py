# Generated by Django 3.0.6 on 2020-05-31 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200531_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_register',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task_register',
            name='critical_points',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
