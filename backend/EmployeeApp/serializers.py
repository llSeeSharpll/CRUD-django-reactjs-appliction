from django.db.models import fields
from rest_framework import serializers
from .models import *

#serializer for the department model
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('departmentId',
                  'departmentName')

#serializer for the employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employeeId',
                  'employeeName',
                  'department',
                  'dateOfJoin',
                  'get_photo',
                  'get_department')