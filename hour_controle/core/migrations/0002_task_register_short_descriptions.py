# Generated by Django 3.0.6 on 2020-05-31 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_register',
            name='short_descriptions',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
