from django.shortcuts import render
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view


from .models import *
from .serializers import *

#api call for the department model
@csrf_exempt
def departmentApi(request, id = 0):
    if request.method == 'GET':#get request
        departments =  Departments.objects.all()#gets all the department entriez
        department_serializer = DepartmentSerializer(departments, many = True)
        return JsonResponse(department_serializer.data, safe = False)
    if request.method == 'POST':#post request
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data = department_data)
        if department_serializer.is_valid():#check if serialzed data is valid
            department_serializer.save()#save the object into sqlite database
            return JsonResponse("Added successfull", safe = False)
        return JsonResponse("Error happened, please try again later!", safe = False)
    if request.method == 'PUT':#put request to update department data
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(departmentId = department_data['departmentId'])#get the departemtn object
        department_serializer = DepartmentSerializer(department, department_data)
        if department_serializer.is_valid():#check if serializer is valid
            department_serializer.save()#save the changes to sqlite database
            return JsonResponse("Update complete!!", safe = False)
        return JsonResponse("Error happened please try again later", safe = False)
    if request.method == 'DELETE':# a delete request to delete a specific deparatmen
        department = Departments.objects.get(departmentId = id)#get method from sqlite to get a specific department object
        department.delete()#delete function from the sqlite database for a specific department
        return JsonResponse("Delete successfull!!", safe = False)

#api for the employee
@api_view(['POST','GET','PUT','DELETE'])
def employeeApi(request, id = 0):
    if request.method == 'GET':#get method to get all employees
        employees =  Employees.objects.all()#get function that returns all the entries in table employees
        employee_serializer = EmployeeSerializer(employees, many = True)
        return JsonResponse(employee_serializer.data, safe = False)
    if request.method == 'POST':#post request to add employees to the database
        #get the data from the request header
        employee_name = request.data.get('employeeName')
        employee_department = request.data.get('department')
        employee_photo = request.data.get('photo')
        #get the department entry from database based on the name
        department = Departments.objects.get(departmentName = employee_department)
        #make a new employees class and adds the information needed
        employee = Employees()
        employee.employeeName = employee_name
        employee.department = department
        if employee_photo is not None:#check if the photo given or not
            employee.photo = employee_photo
        if employee is not None:#check if employee actaully exsists/name given departement...
            employee.save()#save function to save data in sqlite database
            return JsonResponse("Added successfull", safe = False)
        return JsonResponse("Error happened, please try again later!", safe = False)
    if request.method == 'PUT':#a put method to update exsisting employees
        #get data from the request
        employee_Id = request.data.get('employeeId')
        employee_name = request.data.get('employeeName')
        employee_department = request.data.get('department')
        employee_photo = request.data.get('photo') 
        #get the employee that will be updated based on the id
        employee = Employees.objects.get(employeeId = employee_Id)
        #check what given fields are given tobe updated and saves the new data to the database
        if employee_department is not None and employee_name is not None and employee_photo is not None:
            department = Departments.objects.get(departmentName=employee_department)
            employee.employeeName = employee_name
            employee.department = department
            employee.photo = employee_photo 
            employee.save()
            return JsonResponse("Update complete!!", safe = False)
        if employee_department is not None and employee_name is not None:
            department = Departments.objects.get(departmentName=employee_department)
            employee.employeeName = employee_name
            employee.department = department
            employee.save()
            return JsonResponse("Update complete!!", safe = False)
        if employee_department is not None and employee_photo is not None:
            department = Departments.objects.get(departmentName=employee_department)
            employee.department = department
            employee.photo = employee_photo 
            employee.save()
            return JsonResponse("Update complete!!", safe = False)
        if employee_name is not None and employee_photo is not None:
            employee.employeeName = employee_name
            employee.photo = employee_photo 
            employee.save()
            return JsonResponse("Update complete!!", safe = False)
        if employee_name is not None:
            employee.employeeName = employee_name
            employee.save()
            return JsonResponse("Update complete!!", safe = False)
        if employee_photo is not None:
            employee.photo = employee_photo
            employee.save()
            return JsonResponse("Update complete!!", safe = False)
        if employee_department is not None:
            department = Departments.objects.get(departmentName=employee_department)
            employee.department = department
            employee.save()
            return JsonResponse("Update complete!!", safe = False)
        return JsonResponse("Error happened please try again later", safe = False)
    if request.method == 'DELETE':#delete function to delete a specific employee
        employee = Employees.objects.get(employeeId = id)#get the employee entry based on the id
        employee.delete()#delete function that deletes the entry given
        return JsonResponse("Delete successfull!!", safe = False)
