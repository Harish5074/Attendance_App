import xlwt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from .models import AttendanceRecord, IssueTable, Employee
from .serializers import AttendancerecordSeriakizer, IssueTableSerializer, EmployeeSerilizer
from datetime import datetime, timedelta
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
'''
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes({IsAuthenticated})
'''
@api_view(['GET'])
def employee_HomePage(request):
    emps = Employee.objects.all()
    empsser = EmployeeSerilizer(emps, many=True)
    return Response(empsser.data)


@api_view(['GET'])
def employee_Details(request, id):
    emp = get_object_or_404(Employee, pk=id)
    empser = EmployeeSerilizer(emp, many=False)
    return Response(empser.data)


@api_view(['POST'])
def employee_Create(request):
    empser = EmployeeSerilizer(data=request.data)
    if empser.is_valid():
        empser.save()
    return Response(empser.data)


@api_view(['POST'])
def employee_Update(request, id):
    emp = get_object_or_404(Employee, pk=id)
    empser = EmployeeSerilizer(instance=emp, data=request.data)
    if empser.is_valid():
        empser.save()
    return Response(empser.data)


@api_view(['DELETE'])
def employee_Delete(request, id):
    emp = get_object_or_404(Employee, pk=id)
    emp.delete()
    return Response("Employee detail is deleted successfully")


# Attendance module

@api_view(['GET'])
def atd_HomePage(request):
    atds = AttendanceRecord.objects.all()
    atdsser = AttendancerecordSeriakizer(atds, many=True)
    return Response(atdsser.data)


@api_view(['GET'])
def atd_Details(request, id):
    atd = get_object_or_404(AttendanceRecord, pk=id)
    atdser = AttendancerecordSeriakizer(atd, many=False)
    return Response(atdser.data)


@api_view(['POST'])
def atd_Create(request):
    atdser = AttendancerecordSeriakizer(data=request.data)
    if atdser.is_valid():
        atdser.save()
    return Response(atdser.data)


@api_view(['POST'])
def atd_Update(request, id):
    atd = get_object_or_404(AttendanceRecord, pk=id)
    atdser = AttendancerecordSeriakizer(instance=atd, data=request.data)
    if atdser.is_valid():
        atdser.save()
    return Response(atdser.data)


@api_view(['DELETE'])
def atd_Delete(request, id):
    atd = get_object_or_404(AttendanceRecord, pk=id)
    atd.delete()
    return Response("Attendance Record is deleted successfully")


# Issue Tracker


@api_view(['GET'])
def isu_HomePage(request):
    isus = IssueTable.objects.all()
    isusser = IssueTableSerializer(isus, many=True)
    return Response(isusser.data)


@api_view(['GET'])
def isu_Details(request, id):
    isu = get_object_or_404(IssueTable, pk=id)
    isuser = IssueTableSerializer(isu, many=False)
    return Response(isuser.data)


@api_view(['POST'])
def isu_Create(request):
    isuser = IssueTableSerializer(data=request.data)
    if isuser.is_valid():
        isuser.save()
    return Response(isuser.data)


@api_view(['POST'])
def isu_Update(request, id):
    isu = get_object_or_404(IssueTable, pk=id)
    isuser = IssueTableSerializer(instance=isu, data=request.data)
    if isuser.is_valid():
        isuser.save()
    return Response(isuser.data)


@api_view(['DELETE'])
def isu_Delete(request, id):
    isu = get_object_or_404(IssueTable, pk=id)
    isu.delete()
    return Response("Issue tracker detail is deleted successfully")


def userdetails(request, id):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    # decide file name
    response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    # adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    # column header names, you can use your own headers here
    columns = ['From Date', 'To Date', 'Status', 'Employee Name', ]

    # write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    user = Employee.objects.get(pk=id)
    atrecord = user.attendancerecord_set.filter(fromdate__gte=(datetime.now() - timedelta(days=30)))
    data = AttendancerecordSeriakizer(atrecord, many=True).data

    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row["fromdate"], font_style)
        ws.write(row_num, 1, my_row["todate"], font_style)
        ws.write(row_num, 2, my_row["status"], font_style)
        ws.write(row_num, 3, user.name, font_style)

    wb.save(response)
    return response
