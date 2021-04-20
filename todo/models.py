from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import date

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    Due_Date = models.DateField(null=False, blank=False)


    def __str__(self):
        return self.title
    
    @property
    def is_past_due(self):
        return date.today() > self.Due_Date

    class Meta:
        ordering = ['complete']