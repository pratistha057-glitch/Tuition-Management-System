from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    ROLE = [
        ("ADMIN", "Admin"),
        ("TEACHER", "Teacher"),
        ("STUDENT", "Student"),
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE)
    image = models.ImageField(upload_to="profile_images/",null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    class Meta:
        db_table = "user_profile"
