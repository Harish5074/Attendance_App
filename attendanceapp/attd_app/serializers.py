from rest_framework import serializers
from .models import AttendanceRecord, IssueTable,Employee

class AttendancerecordSeriakizer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceRecord
        fields = '__all__'


class IssueTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = IssueTable
        fields = '__all__'


class EmployeeSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'