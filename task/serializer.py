# tasks/serializers.py

from rest_framework import serializers
from .models import Employee, Task, TaskAssignment

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description')

class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = ('id', 'task', 'assigned_to', 'date_assigned')
