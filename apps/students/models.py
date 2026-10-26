from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    joined_date = models.DateField(auto_now_add=True)
    class_name = models.CharField(max_length=30)
    course = models.ForeignKey("courses.Course",on_delete=models.SET_NULL,null=True,blank=True)
    batch = models.ForeignKey("courses.Batch",on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f"{self.student_id} - {self.user.username}"

    class Meta:
        db_table = "students"
