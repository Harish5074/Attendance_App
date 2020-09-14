from django.db import models


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + " - " + self.name


class AttendanceRecord(models.Model):
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    status = models.CharField(max_length=15)
    Employ = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.Employ.name + " attendance for date" + self.todate.date().strftime("%d-%b-%y")


class IssueTable(models.Model):
    employ = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #month = models.ForeignKey()
    Comments = models.CharField(max_length=500)


    def __str__(self):
        return self.employ.name + " Issue raised."

