

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Activity, Course


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['url', 'informations', 'code',
                  'open', 'hidden', 'path', 'course']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'name', 'description', 'path', 'code', 'activities']
