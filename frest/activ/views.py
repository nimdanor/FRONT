from operator import imod
from django.shortcuts import render
from rest_framework import viewsets


from .models import Activity, Course
from .serializers import ActivitySerializer, CourseSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
