# Generated by Django 3.2 on 2021-04-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Due_Date',
            field=models.DateField(),
        ),
    ]
