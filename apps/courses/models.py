from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#Course Model (Main)
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    fee = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "courses"




#Subject model
class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.course.name} - {self.name}"

    class Meta:
        db_table = "subjects"




#Batch Model
class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="batches")
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "batches"
