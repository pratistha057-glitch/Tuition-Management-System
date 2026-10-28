
from django.contrib import admin
from apps.payments.models import PaymentModel


@admin.register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'fee',
        'amount',
        'payment_method',
        'status',
        'pidx',
        'transaction_id',
        'payment_date',
    )

    list_filter = (
        'status',
        'payment_method',
        'payment_date',
    )

    search_fields = (
        'student__student_name',
        'pidx',
        'transaction_id',
    )

    readonly_fields = (
        'payment_date',
        'pidx',
        'transaction_id',
    )
