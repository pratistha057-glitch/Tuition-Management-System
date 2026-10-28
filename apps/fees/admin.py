from django.contrib import admin
from .models import FeesModel


@admin.register(FeesModel)
class FeesModelAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'course',
        'total_amount',
        'paid_amount',
        'remaining_amount',
        'due_date',
        'status',
    )

    list_filter = (
        'status',
        'due_date',
        'course',
    )

    search_fields = (
        'student__student_id',
        'student__user__username',
        'course__name',
    )

    readonly_fields = (
        'remaining_amount',
    )