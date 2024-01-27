from django.db import models

# Create your models here.
# tasks/models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} assigned to {self.assigned_to.name}"
