from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    path = models.FilePathField(path="/tmp/courses/")
    code = models.JSONField(default=dict)

    def get_path(self):
        return self.path.path


class Activity(models.Model):
    informations = models.TextField()

    open = models.BooleanField(default=True)
    hidden = models.BooleanField(default=False)
    path = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="activities")
    code = models.JSONField(default=dict)
