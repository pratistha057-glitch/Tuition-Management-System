from django.db import models
from apps.students.models import Student
from apps.courses.models import Course
# Create your models here.
class Status(models.TextChoices):
    PAID = 'Paid', 'paid'
    PARTIALLY_PAID = 'Partially Paid', 'partially paid'
    PENDING = 'Pending', 'pending'

class FeesModel(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_profile")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="courses")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='total_amount')
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='paid_amount')
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="remaining_amount")
    due_date = models.DateField(verbose_name="due_date")
    status = models.CharField(max_length=30, choices=Status, default=Status.PENDING, null=False, blank=False, verbose_name='status')



    def save(self, *args, **kwargs):
        self.remaining_amount = self.total_amount - self.paid_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - Remaining: {self.remaining_amount}"

    class Meta:
        db_table="fees"
    