from django.shortcuts import render
# tasks/views.py
from rest_framework import generics
from rest_framework import viewsets
from .models import Employee, Task, TaskAssignment
from .serializer import EmployeeSerializer, TaskSerializer, TaskAssignmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

    def create(self, request, *args, **kwargs):
        task_id = request.data.get('task')
        employee_id = request.data.get('employee')

        try:
            task = Task.objects.get(id=task_id)
            employee = Employee.objects.get(id=employee_id)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=404)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=404)

        assignment_data = {
            'task': task_id,
            'assigned_to': employee_id,
        }

        serializer = self.get_serializer(data=assignment_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

