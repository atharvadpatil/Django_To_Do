# Generated by Django 3.2 on 2021-04-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Due_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]