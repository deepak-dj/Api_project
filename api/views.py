from django.shortcuts import render

from .serializers import employeeSerializers,register_serializers
from .models import employee
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class employeeView(ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeSerializers
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class register_view(ModelViewSet):
        queryset = User.objects.all()
        serializer_class = register_serializers