"""attendanceapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.employee_HomePage, name="EmpHomepage"),
    url(r"^EmpDetails/(?P<id>[0-9]+)/", views.employee_Details, name="EmpDetails"),
    url(r"^EmpCreate/", views.employee_Create, name="EmpCreate"),
    url(r"^EmpUpdate/(?P<id>[0-9]+)/", views.employee_Update, name="EmpUpdate"),
    url(r"^EmpDelete/(?P<id>[0-9]+)/", views.employee_Delete, name="EmpDelete"),

    url(r"^All_Attendance/$", views.atd_HomePage, name="AtdHomepage"),
    url(r"^AtdDetails/(?P<id>[0-9]+)/", views.atd_Details, name="AtdDetails"),
    url(r"^AtdCreate/", views.atd_Create, name="AtdCreate"),
    url(r"^AtdUpdate/(?P<id>[0-9]+)/", views.atd_Update, name="AtdUpdate"),
    url(r"^AtdDelete/(?P<id>[0-9]+)/", views.atd_Delete, name="AtdDelete"),

    url(r"^Issuetracker/$", views.isu_HomePage, name="EmpHomepage"),
    url(r"^IsuDetails/(?P<id>[0-9]+)/", views.isu_Details, name="IsuDetails"),
    url(r"^IsuCreate/", views.isu_Create, name="IsuCreate"),
    url(r"^IsuUpdate/(?P<id>[0-9]+)/", views.isu_Update, name="IsuUpdate"),
    url(r"^IsuDelete/(?P<id>[0-9]+)/", views.isu_Delete, name="IsuDelete"),

    url(r"Download_Attendance_Report/(?P<id>[0-9]+)/", views.userdetails, name="userdetails"),
]
