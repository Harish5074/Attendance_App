from django.contrib import admin
from .models import Employee,AttendanceRecord,IssueTable
# Register your models here.

admin.site.register(Employee)
admin.site.register(AttendanceRecord)
admin.site.register(IssueTable)

