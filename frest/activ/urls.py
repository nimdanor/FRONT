
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'Course', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
