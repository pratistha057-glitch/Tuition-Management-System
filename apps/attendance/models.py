from django.db import models
from apps.students.models import Student


class Status(models.TextChoices):
    PRESENT = 'Present', 'present'
    ABSENT = 'Absent', 'absent'

# Create your models here.
class AttendanceModel(models.Model):
    student  = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_attendance')
    date = models.DateField()
    status = models.CharField(max_length=20, choices=Status, default=Status.ABSENT, verbose_name="status")

    class Meta:
        db_table = 'attendance'
        constraints = [
            models.UniqueConstraint(fields=['student','date'], name='unique_student_date')
        ]

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"