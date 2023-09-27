from django.shortcuts import render

# Create your views here.

from .models import (School, SSS)
from rest_framework import viewsets, permissions
from .serializers import (SchoolSerializer, SSSSerializer)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]


class SSSViewSet(viewsets.ModelViewSet):
    queryset = SSS.objects.all()
    serializer_class = SSSSerializer
    permission_classes = [permissions.AllowAny]