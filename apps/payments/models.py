from django.db import models
from apps.fees.models import FeesModel
from apps.students.models import Student


class PaymentMethod(models.TextChoices):
    KHALTI = 'Khalti', 'khalti'


class Status(models.TextChoices):
    SUCCESS = 'Success', 'success'
    FAILED = 'Fail', 'fail'
    PENDING = 'Pending', 'pending'


class PaymentModel(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='payment_model_student')
    fee = models.ForeignKey(FeesModel,on_delete=models.CASCADE,related_name='payment_model_fees')
    amount = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='amount')
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices,default=PaymentMethod.KHALTI)
    pidx = models.CharField(max_length=255,blank=True,null=True)
    transaction_id = models.CharField(max_length=40,null=True, blank=True)
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.FAILED)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return f'{self.student} - transaction_id: {self.transaction_id}'
