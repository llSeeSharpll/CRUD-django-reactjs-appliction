from django.conf.urls import url
from django.urls.resolvers import URLPattern

from EmployeeApp import views

urlpatterns = [
    #department urls
    url(r'^department/$',views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),
    #employee url
    url(r'^employee/$',views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi)
]
