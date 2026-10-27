from django.db import models

BATCH_CHOICES = [
    ("Morning", "Morning"),
    ("Afternoon", "Afternoon"),
    ("Evening", "Evening"),
]
# Create your models here.


#Subject model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subjects"




#Course Model (Main)
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    fee = models.PositiveIntegerField()
    subjects = models.ManyToManyField(Subject,related_name="courses",blank=True)
    batch = models.CharField(max_length=20,choices=BATCH_CHOICES,default="Morning")


    def __str__(self):
        return f"{self.name} - {self.batch}"

    class Meta:
        db_table = "courses"




