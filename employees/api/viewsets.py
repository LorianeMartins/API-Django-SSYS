from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from employees.api import serializers
from employees import models


class EmployeesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.EmployeesSerializer
    queryset = models.Employees.objects.all()
    