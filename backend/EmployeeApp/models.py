from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User

#department model that saved as a table in sqlite database
class Departments(models.Model):
    departmentId = models.AutoField(primary_key = True)
    departmentName = models.CharField(max_length = 100)
    class Meta:
        ordering = ('departmentName',)

    #returns the department name as a sstring
    def __str__(self):
        return self.departmentName

#employee model that saved as a table in sqlite
class Employees(models.Model):
    employeeId = models.AutoField(primary_key = True)
    employeeName = models.CharField(max_length = 25)
    department = models.ForeignKey(Departments, related_name='employeee', on_delete=models.CASCADE)
    dateOfJoin = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='uploads/', blank=True, null=True)

    #ordering the entries by the date of join
    class Meta:
        ordering = ('-dateOfJoin',)

    #return the employee name as a string
    def __str__(self):
        return self.employeeName

    #return the photo as a url
    def get_photo(self):
        if self.photo:
            return "http://127.0.0.1:8000"+self.photo.url;
        return ""
    
    #return the department name from the department model
    def get_department(self):
        return self.department.departmentName
